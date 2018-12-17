from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    dni = forms.CharField(max_length=9, required=True, help_text='Required')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'dni', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class SignUpUserForm(SignUpForm):
    born_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'dni', 'born_date', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class SignUpMedicForm(SignUpForm):
    plate = forms.CharField(max_length=8, required=False, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'dni', 'plate', 'first_name', 'last_name', 'email', 'password1', 'password2',)

