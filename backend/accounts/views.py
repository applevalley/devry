import json
import requests

from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from allauth.account.forms import ResetPasswordForm
from allauth.account.utils import complete_signup
from allauth.account.views import ConfirmEmailView

from rest_framework import status, generics, permissions, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import CreateAPIView, UpdateAPIView, GenericAPIView, RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from rest_auth.app_settings import (TokenSerializer,
                                    JWTSerializer,
                                    create_token)
from rest_auth.models import TokenModel
from rest_auth.registration.views import RegisterView
from rest_auth.utils import jwt_encode
from rest_auth.views import LoginView, LogoutView

from django.conf import settings
from django.contrib.auth import get_user_model, authenticate, login as django_login, logout as django_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail.message import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.http import require_POST

from .models import User, TokenModel, UserFollowing
from .serializers import UserRegistrationSerializer, UserSerializer, InfoSerializer, isfollowingSerializer, \
    deleteSerializer, UserLoginSerializer, UserFollowersSerializer, UserFollowingSerializer, TokenSerializer, \
    UserFollowerNumberSerializer, UserFollowingNumberSerializer, UserFollowSerializer
from .app_settings import RegisterSerializer, register_permission_classes
from mysite.app_settings import TokenSerializer, LoginSerializer, UserDetailsSerializer, JWTSerializer, create_token
from mysite.utils import jwt_encode
from profiles.models import Profile
from profiles.serializers import ProfileSerializer, ProfileShowSerializer


sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters('password1', 'password2')
)


sensitive_post_parameters_n = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2'
    )
)


class UserSignupView(CreateAPIView):
    """
    유저네임, 이메일, 비밀번호를 입력해 가입할 수 있습니다.
    """
    serializer_class = UserRegistrationSerializer
    permission_classes = register_permission_classes()
    token_model = TokenModel

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(UserSignupView, self).dispatch(*args, **kwargs)

    def get_response_data(self, user):
        if allauth_settings.EMAIL_VERIFICATION == \
                allauth_settings.EmailVerificationMethod.MANDATORY:
            return {"detail": _("Verification e-mail sent.")}

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': user,
                'token': self.token
            }
            # return JWTSerializer(data).data
            return {"Registration": "OK"}
        else:
            # TokenSerializer(user.auth_token).data 로 사용자의 토큰에 접근할 수 있습니다.
            return {"Registration": "OK"}

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(self.get_response_data(user),
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        if getattr(settings, 'REST_USE_JWT', False):
            self.token = jwt_encode(user)
        else:
            create_token(self.token_model, user, serializer)

        complete_signup(self.request._request, user,
                        allauth_settings.EMAIL_VERIFICATION,
                        None)
        return user


class UserLoginView(GenericAPIView):
    """
    이메일과 비밀번호를 통해 토큰을 발급받을 수 있습니다.

    ---
    """
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    token_model = TokenModel

    @sensitive_post_parameters_n
    def dispatch(self, *args, **kwargs):
        return super(UserLoginView, self).dispatch(*args, **kwargs)

    def process_login(self):
        django_login(self.request, self.user)

    def get_response_serializer(self):
        if getattr(settings, 'REST_USE_JWT', False):
            response_serializer = JWTSerializer
        else:
            response_serializer = TokenSerializer
        return response_serializer

    def login(self):
        self.user = self.serializer.validated_data['user']
        if getattr(settings, 'REST_USE_JWT', False):
            self.token = jwt_encode(self.user)
        else:
            self.token = create_token(self.token_model, self.user,
                                      self.serializer)
        if getattr(settings, 'REST_SESSION_LOGIN', True):
            self.process_login()

    def get_response(self):
        serializer_class = self.get_response_serializer()
        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': self.user,
                'token': self.token
            }
            serializer = serializer_class(instance=data,
                                          context={'request': self.request})
        else:
            serializer = serializer_class(instance=self.token,
                                          context={'request': self.request})
        token = Token.objects.all()
        user_token = Token.objects.get(user_id=self.user.id)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        print(token)
        response = Response({
            "user": {
                "id": self.user.id,
                "username": self.user.username,
            },
            "token": serializer.data['key']
        })

        # 사용자의 프로필이 존재하는 경우 로그인시 프로필의 tag 정보를 추가하는 과정
        profiles = Profile.objects.all()
        if profiles.filter(user_id=self.user.id).exists():
            profile = Profile.objects.get(username=self.user.username)
            if ProfileSerializer(profile).data['my_tags']:
                user_tag = ProfileSerializer(profile).data['my_tags']
                user_profile_img = ProfileSerializer(
                    profile).data['profile_img']
                response = Response({
                    "user": {
                        "id": self.user.id,
                        "username": self.user.username,
                        "my_tags": user_tag,
                        "profile_img": user_profile_img
                    },
                    "token": serializer.data['key']
                })

        if getattr(settings, 'REST_USE_JWT', False):
            from rest_framework_jwt.settings import api_settings as jwt_settings
            if jwt_settings.JWT_AUTH_COOKIE:
                from datetime import datetime
                expiration = (datetime.utcnow() +
                              jwt_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(jwt_settings.JWT_AUTH_COOKIE,
                                    self.token,
                                    expires=expiration,
                                    httponly=True)
        return response

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data,
                                              context={'request': request})
        self.serializer.is_valid(raise_exception=True)
        self.login()
        return self.get_response()


class UserLogoutView(LogoutView):
    """
    headers에 유저의 토큰을 입력합니다. 
    headers={'Authorization': 'Token your_token'}
    """

    def post(self, request):
        if request.META.get('HTTP_AUTHORIZATION'):
            tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
            user = User.objects.get(id=tok.user_id)
            request.user = user
        Token.objects.get(user_id=request.user.pk).delete()
        # TokenSerializer(request.user.auth_token).remove()
        return Response('로그아웃되었습니다', status=status.HTTP_204_NO_CONTENT)


class UserInfoView(APIView):
    """
    이메일과 유저네임을 통해 특정 유저의 정보를 얻을 수 있습니다. 
    {
        "username": "username",
        "email": "email"
    }
    """

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            serializer = InfoSerializer(data=request.data)
            email = request.data.get('email')
            username = request.data.get('username')
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None":
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)

        response = {
            'user': {
                'username': serializer.data['username'],
                'email': serializer.data['email'],

            },
        }
        return Response(response, status=status.HTTP_200_OK)


class UserFollowingViewSet(viewsets.ModelViewSet):
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowingSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)


@api_view(['GET', 'POST'])
def following(request):
    '''
    GET Method의 경우 모든 팔로잉 정보를, 
    POST Method의 경우 팔로잉이 이루어집니다.
    입력 값은 다음과 같고, user는 following_user를 팔로우합니다.
    {
        'user': user_pk,
        'following_user': user_pk
    }
    '''
    if request.method == 'GET':
        follows = UserFollowing.objects.all()
        serializer = UserFollowingSerializer(follows, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserFollowingSerializer(data=request.data)
        followee_people = User.objects.get(pk=request.data['user'])
        following_people = User.objects.get(pk=request.data['following_user'])

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        followee_people.follower_num += 1
        following_people.followee_num += 1
        followee_people.save()
        following_people.save()

        return Response(serializer.data)


@api_view(['GET', 'POST'])
def follow_list(request):
    if request.method == 'GET':
        follows = UserFollowing.objects.all()
        serializer = UserFollowingSerializer(follows, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def following_list(request):
    if request.method == 'GET':
        pass
    else:
        serializer = UserFollowingSerializer(data=request.data)
        followee_people = User.objects.get(pk=request.data['user'])
        following_people = User.objects.get(pk=request.data['following_user'])

        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            serializer.save()
        followee_people.follower_num += 1
        following_people.followee_num += 1
        followee_people.save()
        following_people.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def followee_list(request):
    if request.method == 'GET':
        pass
    else:
        serializer = UserFollowingSerializer(data=request.data)
        followee_people = User.objects.get(pk=request.data['user'])
        following_people = User.objects.get(pk=request.data['following_user'])
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            serializer.save()
        followee_people.follower_num += 1
        following_people.followee_num += 1
        followee_people.save()
        following_people.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def myfollower_list(request):
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        my = User.objects.get(id=tok.user_id)
        request.user = my

    if request.method == 'GET':
        follows = UserFollowing.objects.all()
        fos = follows.filter(following_user=request.user.pk)
        for fo in fos:
            if UserFollowing.objects.filter(following_user=fo.user, user=request.user.pk).exists():
                fo.is_following = "True"
            else:
                fo.is_following = "False"
            fo.save()
        serializer = isfollowingSerializer(fos, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def myfollow_list(request):
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        my = User.objects.get(id=tok.user_id)
        request.user = my

    if request.method == 'GET':
        follows = UserFollowing.objects.all()
        fos = follows.filter(user=request.user.pk)
        for fo in fos:
            if UserFollowing.objects.filter(user=request.user.pk).exists():
                fo.is_following = "True"
            else:
                fo.is_following = "False"
            fo.save()
        serializer = isfollowingSerializer(fos, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def yourfollower_list(request, want_pk):
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        my = User.objects.get(id=tok.user_id)
        request.user = my

    if request.method == 'GET':
        follows = UserFollowing.objects.all()
        fos = follows.filter(following_user=want_pk)
        for fo in fos:
            target = fo.user
            if UserFollowing.objects.filter(user=request.user.pk, following_user=target).exists():
                fo.is_following = "True"
            else:
                fo.is_following = "False"
            fo.save()
        serializer = isfollowingSerializer(fos, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def yourfollow_list(request, want_pk):
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        my = User.objects.get(id=tok.user_id)
        request.user = my

    if request.method == 'GET':
        follows = UserFollowing.objects.all()
        fos = follows.filter(user=want_pk)
        for fo in fos:
            target = fo.following_user
            if UserFollowing.objects.filter(user=request.user.pk, following_user=target).exists():
                fo.is_following = "True"
            else:
                fo.is_following = "False"
            fo.save()
        serializer = isfollowingSerializer(fos, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def toggle_following(request, want_pk):
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        my = User.objects.get(id=tok.user_id)
        request.user = my
    # user authentication process

    if request.method == 'GET':
        if UserFollowing.objects.filter(following_user=want_pk, user=request.user.pk).exists():
            fo = UserFollowing.objects.get(
                following_user=want_pk, user=request.user.pk)
            fo.is_following = "True"
            serializer = isfollowingSerializer(fo)
            return Response(serializer.data)
        else:
            return Response("false")

    if request.method == 'POST':
        if UserFollowing.objects.filter(following_user=want_pk, user=request.user.pk).exists():
            # following canceled
            followee_people = User.objects.get(pk=request.user.pk)
            following_people = User.objects.get(pk=want_pk)
            followee_people.followee_num -= 1
            following_people.follower_num -= 1
            followee_people.save()
            following_people.save()
            UserFollowing.objects.get(
                following_user=want_pk, user_id=request.user.pk).delete()

            followee_people_id = UserSerializer(followee_people).data['id']
            following_people_profile = Profile.objects.get(
                username=following_people)

            if UserSerializer(following_people).data['followers'] == []:
                following_people_profile.is_following = False
            else:
                for single_user in UserSerializer(following_people).data['followers']:
                    if followee_people_id == single_user['user']:
                        following_people_profile.is_following = True
                    else:
                        following_people_profile.is_following = False

            following_people_profile.follower_num = following_people.follower_num
            following_people_profile.save()

            return Response("following canceled")
        else:
            # following
            serializer = UserFollowingSerializer(data=request.data)
            followee_people = User.objects.get(pk=request.user.pk)
            following_people = User.objects.get(pk=want_pk)
            user = request.user.pk
            following_user = want_pk
            a = {"user": user, "following_user": following_user}
            serializer = UserFollowingSerializer(data=a)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            followee_people.followee_num += 1
            following_people.follower_num += 1
            followee_people.save()
            following_people.save()

            followee_people_id = UserSerializer(followee_people).data['id']
            following_people_profile = Profile.objects.get(
                username=following_people)

            if UserSerializer(following_people).data['followers'] == []:
                following_people_profile.is_following = False
            else:
                for single_user in UserSerializer(following_people).data['followers']:
                    if followee_people_id == single_user['user']:
                        following_people_profile.is_following = True
                    else:
                        following_people_profile.is_following = False

            following_people_profile.follower_num = following_people.follower_num
            following_people_profile.save()

            return Response("following ")


class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'  # 템플릿을 변경하려면 이와같은 형식으로 입력
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm

    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            return render(self.request, 'accounts/password_reset_done_fail.html')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'  # 템플릿을 변경하려면 이와같은 형식으로 입력


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = SetPasswordForm
    success_url = reverse_lazy('password_reset_complete')
    template_name = 'accounts/password_reset_confirm.html'

    def form_valid(self, form):
        return super().form_valid(form)


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_url'] = resolve_url(settings.LOGIN_URL)
        return context


@api_view(['GET', 'DELETE'])
@permission_classes([AllowAny])
def delete(request):
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        my = User.objects.get(id=tok.user_id)
        request.user = my

    if request.method == 'DELETE':
        info = request.user
        info.delete()
        return Response({'email': info.email}, status=status.HTTP_204_NO_CONTENT)
    return Response("회원탈퇴 페이지입니다")
