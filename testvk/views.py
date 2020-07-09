from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, PasswordForm
from .models import User
import logging
from django.db import connection


logger = logging.getLogger(__name__)


class FormWrapper:
    def __init__(self, form, error=False):
        self.form = form
        self.error = error


def register(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = User()
            user.Email = signup_form.data.get("email", None)
            user.Login = signup_form.data.get("username", None)
            user.Password = signup_form.data.get('password', None)
            user.save()
            return redirect('login')
        else:
            signup_form = FormWrapper(signup_form, True)
            login_form = FormWrapper(LoginForm())
            return render(request, 'register.html', {'signup_form': signup_form, 'login_form': login_form})
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.data.get("email", None)
            password = login_form.data.get("password", None)
            user = User.objects.filter(Email=email, Password=password).first()
            if user is not None:
                request.session['user_id'] = user.id
                return redirect('user_page')
    return render(request, 'login.html')
