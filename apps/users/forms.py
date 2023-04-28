from captcha.fields import ReCaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

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


class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField()

    def clean(self):
        captcha = self.cleaned_data.get("captcha")
        if not captcha:
            return
        return super().clean()


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)
