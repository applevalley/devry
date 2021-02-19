import json
import requests 
import os

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.serializers import UserSerializer, UserProfileUpdateSerializer, TokenSerializer, UserJoinedSerializer, UserFollowerNumberSerializer, UserinfoSerializer
from accounts.models import User
from .serializers import ProfileSerializer, ProfileListSerializer, ProfileLinkSerializer, ProfileProjectSerializer, ProfileUpdateSerializer, ProfileShowSerializer
from .models import Profile
from rest_framework import viewsets

from mysite.utils import jwt_encode
from rest_auth.models import TokenModel
from rest_framework.authtoken.models import Token
from mysite.app_settings import TokenSerializer

from qnas.serializers import QnaSerializer, AnsSerializer, QnapinnedSerializer
from qnas.models import Qna, Ans

from forums.serializers import PostSerializer, CommentSerializer, ForumpinnedSerializer
from forums.models import Post, Comment

from PIL import Image
class PostViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        profile_user = User.objects.get(pk=request.data['user'])
        profile_user_data = {
            # 'username': request.data['username'],
            'email': UserProfileUpdateSerializer(profile_user).data['email'],
        }
        profile_user_serailzer = UserProfileUpdateSerializer(profile_user, data=profile_user_data)

        # print(profile_user_data['username'])
        if profile_user_serailzer.is_valid(raise_exception=True):
            profile_user_serailzer.save()
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def profile_list_create(request):
    '''
    GET Method를 통해 사용자들의 프로필을 조회할 수 있습니다.
    '''
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileListSerializer(profiles, many=True)

        # 프로필에서 저장한 sns_name, sns_url, project_name, project_url들을 각각 link, project에 담아주는 과정입니다.
        profile_number = 0
        for profile in profiles:
            for number in range(1, 4):
                sns_name = 'sns_name' + str(number)
                sns_url = 'sns_url' + str(number)

                project_name = 'project_name' + str(number)
                project_url = 'project_url' + str(number)

                # sns_name(1 ~ 3), sns_url(1 ~ 3)이 존재하는 경우 -- 하나만 존재하는 경우 추가하지 않음
                if ProfileSerializer(profile).data[sns_name] and ProfileSerializer(profile).data[sns_url]:
                    serializer.data[profile_number]['link'].append({ProfileSerializer(profile).data[sns_name]: ProfileSerializer(profile).data[sns_url]})

                # project_name(1 ~ 3), project_url(1 ~ 3)이 존재하는 경우 -- 하나만 존재하는 경우 추가하지 않음
                if ProfileSerializer(profile).data[project_name] and ProfileSerializer(profile).data[project_url]:
                    serializer.data[profile_number]['project'].append({ProfileSerializer(profile).data[project_name]: ProfileSerializer(profile).data[project_url]})
            # 1, 2, 3처럼 순서대로 가는 것이 아니라 1, 2, 4번 유저의 프로필이 있고 3번 유저의 프로필이 없는 경우 serializer.data의 인덱스에 연속적인 숫자를 사용하면 인덱스 에러 발생
            profile_number += 1  

        return Response(serializer.data)
        


@api_view(['GET'])
def profile_show(request, profile_pk):
    '''
    GET Method를 통해 사용자의 상세 프로필을 조회합니다. 
    '''
    profile = get_object_or_404(Profile, pk=profile_pk) 
    
    real_tags = {}
    tags_list = {
        'Python3': 0,
        'Django': 0,
        'Java': 0,
        'Spring': 0,
        'HTML5': 0,
        'CSS3': 0,
        'JavaScript': 0,
        'TypeScript': 0,
        'Vue.js': 0,
        'React': 0,
        'Angular': 0,
        'Node.js': 0,
        'Swift': 0,
        'Ruby': 0,
        'Ruby on Rails': 0,
        'MySQL': 0,
        'MariaDB': 0,
        'MongoDB': 0,
        'Docker': 0,
        'Kubernetes': 0,
        'Frontend': 0,
        'Backend': 0,
        'DevOps': 0,
        'Artificial Intelligence': 0,
        'BigData': 0,
        'Blockchain': 0,
        'Internet of Things': 0,
        'Augmented Reality': 0,
        'Virtual Reality': 0
    }

    if request.method == 'GET':
        serializer = ProfileShowSerializer(profile)
        # print(serializer.data)

        # email = User.objects.filter(pk=ProfileSerializer(profile).data['user']).first()
        profile_user = User.objects.get(pk=ProfileSerializer(profile).data['user'])


        serializer.data['followee_num'] = (UserSerializer(profile_user).data['followee_num'])
        serializer.data['follower_num'] = ((UserSerializer(profile_user).data['follower_num']))



        # 모든 qna에서의 글 중 사용자가 쓴 글만 불러오고, 해당 글에서 참조된 태그들을 추가하는 과정
        all_qnas = Qna.objects.filter(user=UserJoinedSerializer(profile).data['id'])
        for some_qna in all_qnas:
            for ref in QnaSerializer(some_qna).data['ref_tags']:
                tags_list[ref] += 1

        # forum에서의 동일한 과정
        all_forums = Post.objects.filter(user=UserJoinedSerializer(profile).data['id'])
        for some_forum in all_forums:
            for ref in PostSerializer(some_forum).data['ref_tags']:
                tags_list[ref] += 1


        # 한 번 이상 추가된 태그들만 남겨놓는 작업

        for single_tag in tags_list:
            if tags_list[single_tag] > 0:
                real_tags[single_tag] = tags_list[single_tag]



        # 팔로잉

        profile_user = User.objects.get(username=ProfileSerializer(profile).data['username'])
        profile_user_id = (ProfileSerializer(profile).data['user'])
        request_user_id = UserinfoSerializer(request.user).data['id']

        # print(profile_user)
        # print(request_user_id)
        # print(request.user_id)
        if request.user != 'AnonymousUser' and request.user != profile_user:
            # if 
            for single_user in UserSerializer(profile_user).data['followers']:
                if request_user_id == single_user['user']:
                    profile.is_following = True
                else:
                    profile.is_following = False



        # # user가 쓴 글들의 수
        user_posts = Post.objects.filter(user=ProfileSerializer(profile).data['user'])
        user_qnas = Qna.objects.filter(user=ProfileSerializer(profile).data['user'])
        profile.post_num = (len(user_posts) + len(user_qnas))
        print(profile.post_num)

        # User정보 안에 저장된 follow 내역들을 profile에 저장하는 과정
        profile.follower_num = profile_user.follower_num
        profile.followee_num = profile_user.followee_num
        profile.save()

        
        # 사용자가 작성한 qna, ans, pinned한 글들만 filter해줌
        qnas = Qna.objects.filter(user=ProfileSerializer(profile).data['user'])
        forums = Post.objects.filter(user=ProfileSerializer(profile).data['user'])
        qna_comments = Ans.objects.filter(user=ProfileSerializer(profile).data['user'])
        forum_comments = Comment.objects.filter(user=ProfileSerializer(profile).data['user'])
    
        user_for_pinned = ProfileSerializer(profile).data['user']
        user_pinned_qnas = []
        qnas_for_pinned = Qna.objects.all()
        for single_pinned_qna in qnas_for_pinned:
            if user_for_pinned in QnapinnedSerializer(single_pinned_qna).data['pinned_users']:
                user_pinned_qnas.append(QnaSerializer(single_pinned_qna).data)
        
        user_pinned_forums = []
        forums_for_pinned = Post.objects.all()
        for single_pinned_forum in forums_for_pinned:
            if user_for_pinned in ForumpinnedSerializer(single_pinned_forum).data['pinned_users']:
                user_pinned_forums.append(PostSerializer(single_pinned_forum).data)



        # 사용자 프로필의 각 필드에 해당 정보들을 추가해서 보여주는 과정
        for qna in qnas:
            serializer.data['qnas'].append(QnaSerializer(qna).data)
        for forum in forums:
            serializer.data['forums'].append(PostSerializer(forum).data)
        for qna_comment in qna_comments:
            serializer.data['qnas_comments'].append(AnsSerializer(qna_comment).data)
        for forum_comment in forum_comments:
            serializer.data['forums_comments'].append(CommentSerializer(forum_comment).data)

            # commented_post = Qna.objects.filter(id=AnsSerializer(comment).data['qna'])
            # print(commented_post)
            print(serializer.data)
            # serializer.data['title'] += 'asdasd'
            
        for pinned_qna in user_pinned_qnas:
            serializer.data['pinned_qnas'].append(pinned_qna)

        for pinned_forum in user_pinned_forums:
            serializer.data['pinned_forums'].append(pinned_forum)

        serializer.data['tags'].update(real_tags)
        # serializer.data['title'].update()
        # print(serializer.data['tags'])

        # 저장된 sns_name, sns_url, project_name, project_url들을 각각 link와 project에 추가해 보여주는 과정
        for number in range(1, 4):
            sns_name = 'sns_name' + str(number)
            sns_url = 'sns_url' + str(number)

            project_name = 'project_name' + str(number)
            project_url = 'project_url' + str(number)

            if ProfileSerializer(profile).data[sns_name] and ProfileSerializer(profile).data[sns_url]:
                serializer.data['link'].append(
                    {
                    'sns_name' : ProfileSerializer(profile).data[sns_name],
                    'sns_url' : ProfileSerializer(profile).data[sns_url]
                    }
                )

            if ProfileSerializer(profile).data[project_name] and ProfileSerializer(profile).data[project_url]:
                serializer.data['project'].append(
                    {
                    'project_name' : ProfileSerializer(profile).data[project_name],
                    'project_url' : ProfileSerializer(profile).data[project_url]
                    }
                )

        print(serializer.data)
        return Response(serializer.data)

 

@api_view(['GET', 'PUT'])
def profile_setting(request, profile_pk):  

    '''
    사용자로부터 넘어오는 토큰 값(request.META['HTTP_AUTHORIZATION'])이 서버에 저장된 사용자의 토큰과 일치하면
    프로필 정보를 보여주거나, 수정할 수 있습니다.
    '''

    # if request.META['HTTP_AUTHORIZATION'] == TokenSerializer(user.auth_token).data['key']:

    profile = get_object_or_404(Profile, pk=profile_pk)
    new_profile = Profile.objects.filter(pk=profile_pk).first()
    if request.META.get('HTTP_AUTHORIZATION'):           
            tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
            user=User.objects.get(id=tok.user_id)
            request.user = user

    links_update = [
    {
        'sns_name': request.data.get('sns_name1', False),
        'sns_url' : request.data.get('sns_url1', False)
    },
    {
        'sns_name': request.data.get('sns_name2', False),
        'sns_url' : request.data.get('sns_url2', False)
    },
    {
        'sns_name': request.data.get('sns_name3', False),
        'sns_url' : request.data.get('sns_url3', False)
    }
    ]

    projects_update = [
    {
        'project_name': request.data.get('project_name1', False),
        'project_url' : request.data.get('project_url1', False)
    },
    {
        'project_name': request.data.get('project_name2', False),
        'project_url' : request.data.get('project_url2', False)
    },
    {
        'project_name': request.data.get('project_name3', False),
        'project_url' : request.data.get('project_url3', False)
    }
    ]

  
    if request.method == 'GET':
        serializer = ProfileListSerializer(profile)
       
        for number in range(1, 4):
            sns_name = 'sns_name' + str(number)
            sns_url = 'sns_url' + str(number)

            project_name = 'project_name' + str(number)
            project_url = 'project_url' + str(number)

            if ProfileSerializer(profile).data[sns_name] and ProfileSerializer(profile).data[sns_url]:
                serializer.data['link'].append(
                    {
                    'sns_name' : ProfileSerializer(profile).data[sns_name],
                    'sns_url' : ProfileSerializer(profile).data[sns_url]
                    }
                )

            if ProfileSerializer(profile).data[project_name] and ProfileSerializer(profile).data[project_url]:
                serializer.data['project'].append(
                    {
                    'project_name' : ProfileSerializer(profile).data[project_name],
                    'project_url' : ProfileSerializer(profile).data[project_url]
                    }
                )
                
        return Response(serializer.data)

    if request.method == 'PUT':
        tags_for_user = ['Python3', 'Django', 'Java','Spring','HTML5','CSS3', 'JavaScript', 'TypeScript','Vue.js','React', 'Angular','Node.js', 'Swift','Ruby','Ruby on Rails', 'MySQL',
        'MariaDB','MongoDB','Docker','Kubernetes','Frontend','Backend','DevOps','Artificial Intelligence','BigData', 'Blockchain','Internet of Things', 'Augmented Reality','Virtual Reality']

        serializer = ProfileUpdateSerializer(instance=profile, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            
        

            # print(serializer.validated_data['my_tags'])
            # for single_tag in request.data['my_tags']:
            #     if single_tag not in tags_for_user:
            #         return Response(serializer.errors)


            # 이미지 받아오기
            # serializer.validated_data['profile_img'] = ''
            # print(request.data)
            # print(serializer.validated_data)
            serializer.validated_data['profile_img'] = request.data['profile_img']


            serializer.validated_data['bio'] = request.data['bio']
            serializer.validated_data['region'] = request.data['region']
            serializer.validated_data['group'] = request.data['group']
            serializer.validated_data['tech_stack'] = request.data['tech_stack']
            serializer.validated_data['my_tags'] = request.data['my_tags']


            serializer.validated_data['links'] = []
            serializer.validated_data['projects'] = []
            
            for link in links_update:
                serializer.validated_data['links'].append(link)
            for project in projects_update:
                serializer.validated_data['projects'].append(project)


            serializer.save(instance=profile, validated_data=serializer.validated_data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
