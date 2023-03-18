# Django
from django import forms

# Local
from .models import Tasks


class TasksForm(forms.ModelForm):
    """Create task form."""
    publisher = forms.CharField(
        label='publisher',
        widget=forms.TextInput(
            attrs={
                'readonly': 'readonly',
                'value': 'Current user',
            }
        )
    )
    class Meta:
        model = Tasks
        exclude = (
            'publisher',
        )