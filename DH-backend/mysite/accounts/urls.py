from django.urls import path
from .views import (
    UserCreateAPI,
    UserLoginAPI, 
    UserProfileAPI,
    UserProfileSettingAPI,
)
urlpatterns = [
    path('login', UserLoginAPI.as_view()),
    path('register', UserCreateAPI.as_view()),
    path('profile/<int:pk>', UserProfileAPI.as_view()),
    path('profile/setting', UserProfileSettingAPI.as_view()),
    
]
