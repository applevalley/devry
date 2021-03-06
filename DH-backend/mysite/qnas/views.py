from django.shortcuts import get_object_or_404
from rest_framework import generics,status, mixins
from .models import Qna,Like
from accounts.models import Profile
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .serializers import (
    QnaRegisterSerializer,
    QnaLikeSerializer,
    QnaDetailSerializer
)
# Create your views here.
class QnaListAPI(generics.ListAPIView):
    serializer_class=QnaDetailSerializer

    def get_queryset(self):
        return Qna.objects.all()

class QnaCreateAPI(generics.CreateAPIView):
    serializer_class=QnaRegisterSerializer
    authentication_classes=[TokenAuthentication]
    def post(self, request):
        
        profile=get_object_or_404(Profile, user=request.user)
        data=request.data.copy()
        data["writer"] = profile.id
        #TODO: vue.js를 통해서 실제로 데이터가 문자열이 아닌 배열로 들어온다면 해당 로직을 바꿔야한다.
        data['ref_tags']='|'.join(data['ref_tags'].split(','))
        serializer = QnaRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QnaDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=QnaDetailSerializer
    def get_queryset(self):
        return Qna.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        qna_id = self.kwargs['pk']
        qna=get_object_or_404(Qna, id=qna_id)
        if qna.writer.id != request.user.get_user_id():
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        qna_id = self.kwargs['pk']
        qna=get_object_or_404(Qna, id=qna_id)
        if qna.writer.id != request.user.get_user_id():
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer=QnaRegisterSerializer(qna, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class QnaLikeAPI(generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    authentication_classes=[TokenAuthentication]
    def post(self, request):
        data = request.data.copy()
        data["user"]=request.user.get_user_id()
        serializer = QnaLikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        context={}
        like=get_object_or_404(Like, user=request.user.get_user_id(), qna=request.data['qna'])
        like.delete()
        context["user"]= request.user.get_username()
        context['qna'] = request.data['qna']
        return Response(context, status=status.HTTP_200_OK)
        # return Response(status=status.HTTP_202_ACCEPTED)