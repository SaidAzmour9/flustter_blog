import django.contrib.auth.models
from django.shortcuts import render, redirect, reverse
import django.urls
from .forms import SignUpForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
# Create your views here.



def signup(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password= password)
            login(request,user)
            return redirect('/accounts')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html',{'form':form})


def profile(request):
    profile = Profile.objects.get(user= request.user)

    return render(request, 'accounts/profile.html', {'profile':profile})



def profile_edit(request):
    if request.method=="POST":
        userform = UserForm(request.POST ,instance=request.user)
        profileform = ProfileForm(request.POST, instance=request.user.profile)
        if userform.is_valid():
            userform.save()
            profileform.save()
            return redirect(reverse('accounts:profile'))

    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=request.user.profile)
    
    
    return render(request, 'accounts/profile_edit.html', {'userform':userform, 'profileform':profileform})
