from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home(request):
    return render(request, 'users/home.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out!!')
    return redirect('home')


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Logged in successfully!!')
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():

        # username = form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password')
        # user = authenticate(username=username, password=password)

        user = form.get_user()

        if user:
            login(request, user)
            messages.success(request, 'Logged in!!')
            return redirect('home')

    return render(request, 'users/user_login.html', {'form': form})
