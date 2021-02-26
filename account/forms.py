from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegistrasiForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'password1','password2']
        labels = {'first_name': 'Nama'}
        help_texts = {
            'username': None,
        }

    def save(self, commit=True):
        user = super(RegistrasiForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']

        if commit:
            user.save()

        return user