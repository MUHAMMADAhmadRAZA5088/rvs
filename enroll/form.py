from dataclasses import field
from django.core import validators
from django import forms
from .models import User


class StudentResistration(forms.ModelForm):
    class Meta:
        model =User
        fields =['Name','Email','password']
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            }