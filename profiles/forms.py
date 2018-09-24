from django import forms
from django.contrib.auth.forms import User
from profiles.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date', 'location', 'bio')