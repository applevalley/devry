from rest_framework import serializers
from .models import (
    Qna,Like
)
from accounts.models import User, Profile

class QnaRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Qna
        fields=['title','content','ref_tags','writer']
    

class QnaDetailSerializer(serializers.ModelSerializer):
    # 필요한 내역: 글 번호, 작성자 정보, ref_tags, (좋아요, 북마크) 수, (좋아요, 북마크) 여부
    writer=serializers.SerializerMethodField()
    ref_tags=serializers.SerializerMethodField()
    like_num=serializers.SerializerMethodField()
    liked=serializers.SerializerMethodField()
    class Meta:
        model=Qna
        fields="__all__"
    
    def get_writer(self, qna):
        user = User.objects.get(id=qna.writer.id)
        profile = Profile.objects.get(user=qna.writer.id)
        return {
            "id" : user.id,
            "username": user.username,
            "email": user.email,
            "profile_img": profile.profile_img
        }

    def get_ref_tags(self, qna):
        return qna.ref_tags.split('|')
    
    def get_like_num(self, qna):
        return len(Like.objects.filter(qna=qna.id))

    def get_liked(self,qna):
        user = self.context.get("request").user
        # 토큰 없이 접근할 경우
        if user.is_anonymous:
            return False

        try:
            # 토큰으로 식별된 user가 해당 qna에 좋아요를 눌렀는지 확인하기
            Like.objects.get(qna=qna.id, user=user.get_user_id())
            return True
        except Like.DoesNotExist :
            return False

class QnaLikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Like
        fields='__all__'