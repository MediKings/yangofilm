from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.db import models
from django.forms import fields


User = get_user_model()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email', 'phone']
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Prénom"}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom"}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Téléphone"}),
        }
