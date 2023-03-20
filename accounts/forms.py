from django import forms
import django.contrib.auth.models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django.db
from .models import Profile



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city','phone_number']