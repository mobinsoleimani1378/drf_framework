from django.urls import path
from . import views
from rest_framework.authtoken import views as token_views

urlpatterns = [
    path('hello', views.Helloworld.as_view()),
    path('articlelist', views.ArticleList.as_view()),
    path('addarticle', views.AddArticleView.as_view()),
    path('checktoken', views.CheckToken.as_view()),
    path('login', token_views.obtain_auth_token),
]
