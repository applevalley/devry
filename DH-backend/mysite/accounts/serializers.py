from rest_framework import serializers
from .models import User, Profile

class UserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['email','username','password']
        
        # post나 put과 같이 데이터를 쓰는 것은 가능하나, 조회는 불가능하게 설정
        extra_kwargs ={
            'password' : {'write_only':True}
        }
    
    # 검증 과정은 프론트엔드에서 하기 때문에 생략
    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        # 비밀번호를 암호화해서 저장하기 위해 반드시 set_password 사용할 것
        user.set_password(self.validated_data['password'])
        user.save()

class UserLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['email','password']
        
        # post나 put과 같이 데이터를 쓰는 것은 가능하나, 조회는 불가능하게 설정
        extra_kwargs ={
            'password' : {'write_only':True}
        }

class UserProfileSerializer(serializers.ModelSerializer):
    user=serializers.SerializerMethodField()
    # tech는 문자열로 저장될 것이기 때문에 분리를 시켜줘야한다.
    tech=serializers.SerializerMethodField()
    # my_tags 역시 마찬가지로 문자열을 분리 시켜줘야한다.
    my_tags=serializers.SerializerMethodField()
    
    # TODO: 차후 구현할 Forum, QnA, Pinned 데이터 등을 get을 통해 노출 시켜줄 필요 있음
    class Meta:
        model=Profile
        fields='__all__'
    def get_user(self, profile):
        user = User.objects.get(email=profile.user)
        return {'id': user.get_user_id(), 'email':str(user), 'username': user.get_username() }
    def get_tech(self, profile):
        return profile.tech.split('|')

    def get_my_tags(self, profile):
        return profile.my_tags.split('|')

class UserProfileSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        # TODO: 프로젝트와 링크 연결할 것
        fields=['region','group','bio','tech','my_tags']