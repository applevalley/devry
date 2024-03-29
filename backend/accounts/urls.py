from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework import routers
from . import views
from .views import UserSignupView, UserLoginView, UserLogoutView, UserInfoView, UserFollowingViewSet

router = routers.DefaultRouter()
router.register('makefollow', UserFollowingViewSet)

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='sign_up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('delete/', views.delete),
    path('info/',  UserInfoView.as_view(), name='info'),
    path('followtest/', include(router.urls)),
    path('follow/', views.following),
    path('follows/', views.follow_list),
    path('following_list/', views.following_list),
    path('followee_list/', views.followee_list),
    path('following/<int:want_pk>/', views.toggle_following),
    path('myfollower/', views.myfollower_list),
    path('myfollow/', views.myfollow_list),
    path('whofollower/<int:want_pk>/', views.yourfollower_list),
    path('whofollow/<int:want_pk>/', views.yourfollow_list),
    
    path('password_reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', views.UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]



