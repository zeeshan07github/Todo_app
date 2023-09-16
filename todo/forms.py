from django import forms
from .models import *


class add_form(forms.ModelForm):
    
    class Meta:
        model = Task
        exclude = ['user']  # Replace 'user' with the name of the field you want to exclude

