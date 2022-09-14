from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class UserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields =  ('username', 'email', 'password1', 'password2', 'portfolio',
'profile_pic', 'first_name', 'last_name')
