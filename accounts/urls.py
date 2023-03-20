from django.urls import path , include
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), # new
    path('profile/', views.profile, name='profile'),
    path('signup', views.signup, name='sign_up'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
]
