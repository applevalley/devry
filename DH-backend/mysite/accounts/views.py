from django.shortcuts import get_object_or_404
from .serializers import (
    UserRegisterSerializer, 
    UserLoginSerializer,
    UserProfileSerializer,
    UserProfileSettingSerializer
)
from django.contrib.auth import authenticate
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .models import User,Profile

# Create your views here.

# 계정 생성 API
class UserCreateAPI(generics.CreateAPIView):
    serializer_class=UserRegisterSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# 계정 로그인 API
class UserLoginAPI(generics.CreateAPIView):
    serializer_class=UserLoginSerializer
    def post(self, request):
        context={}
        email=request.data['email']
        password=request.data['password']
        # 사용자의 정보를 맞추어보고 해당 user가 있으면 반환한다.
        user=authenticate(email=email, password=password)
        
        if user:
            try:
                token=Token.objects.get(user=user)
            except Token.DoesNotExist:
                toekn=Token.objects.create(user=user)
            context['response']="성공적으로 인증되었습니다"
            context['id']=user.id
            context['email']=email
            context['token']=token.key
        else:
            context['response']="에러가 발생했습니다"
            context['error_message']="인증에 실패했습니다"
        return Response(context, status=status.HTTP_404_NOT_FOUND)



class UserProfileAPI(generics.RetrieveAPIView):
    serializer_class=UserProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()
    
        
class UserProfileSettingAPI(generics.UpdateAPIView):
    serializer_class=UserProfileSettingSerializer
    # 토큰을 첨부함으로써 request.user를 통해서 유저 식별이 가능하다.
    authentication_classes=[TokenAuthentication]
    def put(self, request):
        profile=get_object_or_404(Profile, user=request.user)
        # print(request.data)
        if 'tech' in request.data:
            data = request.data.copy()
            #TODO: vue.js를 통해서 실제로 데이터가 문자열이 아닌 배열로 들어온다면 해당 로직을 바꿔야한다.
            # data['tech'] = '|'.join(data['tech']) 
            data['tech'] = '|'.join(data['tech'].split(',')) 
        if 'my_tags' in request.data:
            data = request.data.copy()
            #TODO: vue.js를 통해서 실제로 데이터가 문자열이 아닌 배열로 들어온다면 해당 로직을 바꿔야한다.
            # data['tech'] = '|'.join(data['tech']) 
            data['my_tags'] = '|'.join(data['my_tags'].split(',')) 
        serializer=UserProfileSettingSerializer(profile, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
