from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import User


class UserLoginForm(forms.Form):
    login = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)


class UserSearchForm(forms.Form):
    query = forms.CharField(max_length=128)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)
