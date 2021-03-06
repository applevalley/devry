from django.urls import path
from .views import (
   QnaCreateAPI,
   QnaListAPI,
   QnaLikeAPI,
   QnaDetailAPI,
)
urlpatterns = [
    path('', QnaCreateAPI.as_view()),
    path('list', QnaListAPI.as_view()),
    path('like', QnaLikeAPI.as_view()),
    path('detail/<int:pk>', QnaDetailAPI.as_view()),
]
