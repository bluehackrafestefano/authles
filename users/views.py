import imp
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages\

from .forms import UserForm, UserProfileForm


# Create your views here.
def home(request):
    return render(request, 'users/home.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out!!')
    return redirect('home')


def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()

    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)

        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False)

            profile.user = user
            

    context = {
        'form_user': form_user,
        'form_profile': form_profile,
    }

    return render(request, 'users/register.html', context)