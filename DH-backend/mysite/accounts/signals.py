from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User,Profile, Link, Project
from django.conf import settings
from rest_framework.authtoken.models import Token

# 작성 순서 => __init.py__에 app config default 설정 => apps.py에 ready일 때 import signals 설정
# 이후 원하는 signal 함수를 이곳에 작성하면 된다.

# 계정 생성시 Token 생성
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# 계정 생성시 프로필 생성
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        link    = Link.objects.create(user=instance)
        project = Project.objects.create(user=instance)
        Profile.objects.create(link=link,user=instance, project=project)
