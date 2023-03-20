from blog.urls import app_name
from . import views
from django.urls import path
from .views import article_list, article_detail

app_name = 'articles'


urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('<str:slug>', views.article_detail, name="article_detail"),
]