from . import views
from django.urls import path


app_name = 'blog'

urlpatterns = [
    path('', views.home, name="home"), 
    path('about', views.about, name="about"),
    path('terms', views.terms, name="terms"),
    path('privacy', views.privacy, name="privacy"),
    path('support', views.support, name="support"), 
    
]


