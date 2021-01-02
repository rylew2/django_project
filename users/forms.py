from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # default required=true

    # gives a nested namespace for configurations and keeps them in one place
    class Meta:
        # whenever we do form.save() it will save to User model
        model = User  

        #fields that we want in the form and in what order
        fields = ['username', 'email', 'password1', 'password2']
