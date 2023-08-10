from django.contrib.auth.models import User
from .models import  Profil
from django import forms

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserSingForm(forms.Form):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput)
    password = forms.CharField(label="пароль", widget=forms.PasswordInput)
    def db_login(self):
        cd = self.cleaned_data
        return cd['username'], cd['password']