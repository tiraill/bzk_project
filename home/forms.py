from django.contrib.auth.forms import User
from allauth.account.forms import SignupForm, LoginForm


class MySignupForm(SignupForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class MyLoginForm(LoginForm):
    class Meta:
        model = User
        fields = ('email', 'password')