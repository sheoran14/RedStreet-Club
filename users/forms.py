from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Coach
from django.core.validators import validate_email

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['user_name', 'sport_name', 'post_message', 'registration_date', 'user_profile_link']


class MakeForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['name', 'email', 'sport_name', 'contact', 'city']