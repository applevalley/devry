from django.urls import path, include
from . import views
from rest_framework import routers
from .views import PostViewSet, CommentViewSet


routerq = routers.DefaultRouter()
routerq.register('post', PostViewSet)
routerq.register('comment', CommentViewSet)

urlpatterns = [
    path('forumtest/', include(routerq.urls)),
    path('board/forum/', views.post_list),
    path('board/forumno/', views.post_list_no),

    path('board/forum/new', views.post_list_new),
    path('board/forum/like', views.post_list_like),
    path('board/forum/recommend', views.post_list_recommend),
    path('forum/', views.post_list_create),
    path('forum/<int:post_pk>/', views.post_detail_update_delete),
    path('forum_like/<int:post_pk>/', views.like),
    path('forum_bookmark/<int:post_pk>/', views.bookmark),
    path('forum_pinned/<int:post_pk>/', views.pinned),
    path('forum/mybookmark/', views.forum_mybookmark),
    path('forum/myforum/', views.forum_mypost),
    path('forum/mycomment/', views.forum_mycomment),

    path('comment/', views.comment_list),
    path('comment/<int:comment_pk>/', views.comment_detail_update_delete),
    path('comment_like/<int:comment_pk>/', views.like_comment),
    path('comment/<int:comment_pk>/mentioned/', views.comment_mentioned),
]
