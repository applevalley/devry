from rest_framework import serializers, fields
from .models import Qna, Ans, tech, Qnasmall, Anssmall
from profiles.models import Profile
from profiles.serializers import ProfileSerializer, ProfileListSerializer


class User_infoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qna
        fields = ( 'title', 'written_time', 'ref_tags', 'like_num', 'comment_num', 'viewed_num', 'solved', 'liked')


class ProfileqnaListSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Profile
        fields = ('user', 'username', 'profile_img')


class ProfileqnaSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Profile
        fields = ('user', 'username', 'profile_img', 'bio')
# 'post_num' is_following,is_following추가해야함


class QnasmallSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qnasmall
        fields = ('id', "qna", "content", "userid", "username", "written_time")


class AnssmallSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Anssmall
        fields = ('id', "ans", "content", "userid", "username", "written_time")


class QnaListforamtSerializer(serializers.ModelSerializer):
    
    profile = ProfileqnaListSerializer(
        read_only=True,
    )
    
    class Meta:
        model = Qna
        fields = ('id', 'title', 'written_time', 'ref_tags', 'like_num', 'comment_num', 'viewed_num', 'solved', 'liked', 'profile')


class QnaListSerializer(serializers.ModelSerializer):
    
    profile = ProfileqnaListSerializer(
        read_only=True,
    )
    
    class Meta:
        model = Qna
        fields = ('id', 'title', 'written_time', 'ref_tags', 'like_num', 'comment_num', 'viewed_num', 'solved', 'liked', 'profile')


class AnsdetailSerializer(serializers.ModelSerializer):

    profile = ProfileqnaListSerializer(
        read_only=True,
    )

    anssmall_set = AnssmallSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Ans
        fields = ( 'title', 'assisted', 'like_ans_num', 'content', 'qna', 'written_time', 'liked_ans', 'anssmall_set' ,'profile')


class AnslistSerializer(serializers.ModelSerializer):
    
    profile = ProfileListSerializer(
        read_only=True
    )

    anssmall_set = AnssmallSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Ans
        fields = ( 'title', 'assisted', 'like_ans_num', 'content', 'qna', 'written_time', 'liked_ans', 'anssmall_set' ,'profile')


class AnsSerializer(serializers.ModelSerializer):


    anssmall_set = AnssmallSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Ans
        fields = ( 'title', 'assisted', 'like_ans_num', 'content', 'qna', 'written_time', 'liked_ans', 'anssmall_set', 'profile')


class QnadetailSerializer(serializers.ModelSerializer):

    ref_tags= fields.MultipleChoiceField(choices=tech)
    
    user_set = User_infoSerializer(
        many=True,
        read_only=True,
    )

    profile = ProfileqnaSerializer(
        read_only=True,
    )

    qnasmall_set = QnasmallSerializer(
        many=True,
        read_only=True,
    )

    ans_set = AnsSerializer(
        many=True,
        read_only=True,
        
    )

    ans_count = serializers.IntegerField(
        source='ans_set.count',
        read_only=True,
    )

    class Meta:
        model = Qna
        fields = ('id','profile', 'title','written_time', 'ref_tags', 'solved', 'like_num', 'ans_count',
        'viewed_num', 'bookmark_num','content', 'qnasmall_set', 'ans_set', 'liked', 'bookmarked','user_set' )


class QnaSerializer(serializers.ModelSerializer):

    ref_tags= fields.MultipleChoiceField(choices=tech)
        
    qnasmall_set = QnasmallSerializer(
        many=True,
        read_only=True,
    )

    ans_set = AnsSerializer(
        many=True,
        read_only=True,   
    )

    ans_count = serializers.IntegerField(
        source='ans_set.count',
        read_only=True,
    )

    class Meta:
        model = Qna
        fields = ('id','title', 'profile','content','ref_tags', 'liked', 'like_num', 'bookmarked',
        'solved','bookmark_num', 'viewed_num', 'written_time','ans_set', 'ans_count','qnasmall_set')


class likeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qna
        fields = ('id', "liked")


class like_ansSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ans
        fields = ('id', "liked_ans")


class bookmarkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qna
        fields = ('id', "bookmarked")


class solveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ans
        fields = ('id', "assisted")

  