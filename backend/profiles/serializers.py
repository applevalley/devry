from rest_framework import serializers, fields
from .models import Profile
from .models import tech, user_tag
from accounts.models import User
from django.shortcuts import get_object_or_404

from accounts.serializers import UserSerializer, UserEmailSerializer, UserFollowerNumberSerializer, UserJoinedSerializer, UserFollowingNumberSerializer


class ProfileLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('sns_name1', 'sns_url1', 'sns_name2', 'sns_url2', 'sns_name3', 'sns_url3')


class ProfileProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('project_name1', 'project_url1', 'project_name2', 'project_url2', 'project_name3', 'project_url3')


class ProfileTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('tags',)


class ProfileMyTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('my_tags',)


class ProfileMyTechSerialier(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('tech_stack',)


class ProfileQnaPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('qnas',)

class ProfileForumPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('forums',)


class ProfilePostNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('post_num', )


class ProfilePinnedQnaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('pinned_qnas', )


class ProfilePinnedForumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('pinned_forums', )


class ProfileImageSerializer(serializers.ModelSerializer):
    profile_img = serializers.ImageField()
    class Meta:
        model = Profile
        fields = ('profile_img',)


class ProfileQnaCommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('qnas_comments', )


class ProfileForumCommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('forums_comments', )


class ProfileSerializer(serializers.ModelSerializer):
    tech_stack = fields.MultipleChoiceField(choices=tech)
    my_tags = fields.MultipleChoiceField(choices=user_tag)        

    links = ProfileLinkSerializer(many=True, read_only=True)
    projects = ProfileProjectSerializer(many=True, read_only=True)
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'email', 'username', 'joined', 'follower_num', 'followee_num', 'profile_img', 'region', 'group', 'bio', 'links', 'sns_name1', 'sns_name2', 'sns_name3', 'sns_url1', 'sns_url2', 'sns_url3',
        'tech_stack', 'projects', 'project_name1', 'project_name2', 'project_name3', 'project_url1', 'project_url2', 'project_url3', 'my_tags', 'pinned_qnas', 'qnas',  )



class ProfileShowSerializer(serializers.ModelSerializer):
    link = ProfileLinkSerializer(many=True, read_only=True)
    project = ProfileProjectSerializer(many=True, read_only=True)
    follower_num = serializers.IntegerField(read_only=True)
    followee_num = serializers.IntegerField(read_only=True)

    tags = ProfileTagSerializer(read_only=True)
    qnas = ProfileQnaPostsSerializer(many=True, read_only=True)
    forums = ProfileForumPostsSerializer(many=True, read_only=True)
    
    pinned_qnas = ProfilePinnedQnaSerializer(many=True, read_only=True)
    pinned_forums = ProfilePinnedQnaSerializer(many=True, read_only=True)
    qnas_comments = ProfileQnaCommentsSerializer(many=True, read_only=True)
    forums_comments = ProfileForumCommentsSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ('user', 'email', 'username', 'joined', 'follower_num', 'followee_num', 'profile_img', 'region', 'group', 'bio', 'link', 'is_following',
        'tech_stack', 'my_tags', 'project', 'tags', 'pinned_qnas', 'pinned_forums', 'qnas',  'forums','qnas_comments', 'forums_comments')


class ProfileListSerializer(serializers.ModelSerializer):    
    profile_img = serializers.URLField(read_only=True)
    link = ProfileLinkSerializer(many=True, read_only=True)
    project = ProfileProjectSerializer(many=True, read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    profile_id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = ('email', 'profile_img', 'region', 'group', 'bio', 'link', 'tech_stack', 'project', 'my_tags', 'user_id', 'profile_id', 'username')
        read_only_fields = ('profile_img', 'link', 'project', 'tech_stack')
 

class ProfileUpdateSerializer(serializers.ModelSerializer):
    tech_stack = fields.MultipleChoiceField(choices=tech)
    my_tags = fields.MultipleChoiceField(choices=user_tag)   
    profile_img = serializers.URLField(read_only=True)
    links = fields.ListField()
    projects = fields.ListField()
    class Meta:
        model = Profile
        fields = ( 'username', 'profile_img', 'region', 'group', 'bio', 'links', 'tech_stack', 'projects', 'my_tags',
        'sns_name1', 'sns_name2', 'sns_name3', 'sns_url1', 'sns_url2', 'sns_url3', 'project_name1', 'project_name2', 'project_name3', 'project_url1', 'project_url2', 'project_url3')
        extra_kwargs = {
            'sns_name1': {"write_only": True},
            'sns_name2': {"write_only": True}, 
            'sns_name3': {"write_only": True}, 
            'sns_url1': {"write_only": True},
            'sns_url2': {"write_only": True},
            'sns_url3': {"write_only": True},  
            'project_name1': {"write_only": True},
            'project_name2': {"write_only": True}, 
            'project_name3': {"write_only": True}, 
            'project_url1': {"write_only": True},
            'project_url2': {"write_only": True},
            'project_url3': {"write_only": True},  

        }


    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.profile_img = validated_data.get('profile_img', instance.profile_img)
        instance.region = validated_data.get('region', instance.region)
        instance.group = validated_data.get('group', instance.group)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.links = validated_data.get('links', instance.links)
        instance.tech_stack = validated_data.get('tech_stack', instance.tech_stack)
        instance.projects = validated_data.get('projects', instance.projects)
        instance.my_tags = validated_data.get('my_tags', instance.my_tags)
        instance.sns_name1 = validated_data.get('sns_name1', instance.sns_name1)
        instance.sns_url1 = validated_data.get('sns_url1', instance.sns_url1)
        instance.sns_name2 = validated_data.get('sns_name2', instance.sns_name2)
        instance.sns_url2 = validated_data.get('sns_url2', instance.sns_url2)
        instance.sns_name3 = validated_data.get('sns_name3', instance.sns_name3)
        instance.sns_url3 = validated_data.get('sns_url3', instance.sns_url3)
        instance.project_name1 = validated_data.get('project_name1', instance.project_name1)
        instance.project_url1 = validated_data.get('project_url1', instance.project_url1)
        instance.project_name2 = validated_data.get('project_name2', instance.project_name2)
        instance.project_url2 = validated_data.get('project_url2', instance.project_url2)
        instance.project_name3 = validated_data.get('project_name3', instance.project_name3)
        instance.project_url3 = validated_data.get('project_url3', instance.project_url3)
        instance.save()
        return instance

