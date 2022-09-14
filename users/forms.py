from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
