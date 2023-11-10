from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArticleSer
from rest_framework.authentication import TokenAuthentication
from blog.models import Article


class Helloworld(APIView):
    def get(self, requset):
        name = requset.GET.get('name')
        return Response({"name": name})


class ArticleList(APIView):
    def get(self, request):
        q = Article.objects.all()
        ser = ArticleSer(instance=q, many=True)
        return Response(data=ser.data)


class AddArticleView(APIView):
    def post(self, request):
        ser = ArticleSer(data=request.data)
        if ser.is_valid():
            if request.user.is_authenticated:
                ser.validated_data['user'] = request.user
            ser.save()
            return Response({"respone": "done"})
        return Response(ser.errors)


class CheckToken(APIView):
    def get(self, request):
        user = request.user
        return Response({'user': user.username})
