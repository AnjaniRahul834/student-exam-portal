from django import forms
from django.contrib.auth.models import User
from .models import Task
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'
        