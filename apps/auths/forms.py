# Django
from django import forms

# Local
from .models import Client


class RegistrationForm(forms.ModelForm):
    """Registration form."""

    password2 = forms.CharField(
        label='Repeat password',
        max_length=128,
        required=True
    )
    class Meta:
        model = Client
        fields = (
            'login',
            'password',
            'password2',
        )


class LoginForm(forms.ModelForm):
    """Login form."""

    class Meta:
        model = Client
        fields = (
            'login',
            'password',
        )