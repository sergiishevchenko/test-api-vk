from django import forms
from .models import User


class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=256, help_text='Это поле обязательно')
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput)

    def clean_email(self):
        passed_email = self.cleaned_data.get('email', None)
        if User.objects.filter(email=passed_email).count() > 0:
            raise forms.ValidationError(u'Данный email уже используется.')
        return passed_email

    def clean_username(self):
        passed_username = self.cleaned_data.get('username', None)
        if User.objects.filter(login=passed_username).count() > 0:
            raise forms.ValidationError(u'Данный логин занят.')
        return passed_username


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=256, help_text='Это поле обязательно')
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput)


class PasswordForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='New Password2', widget=forms.PasswordInput)
