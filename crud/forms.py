from django import forms
from .models import Student
from django.core import validators


class User(forms.ModelForm):
    class Meta:                                     # Meta likhte hobe meta naa
        model=Student
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput( render_value=True, attrs={'class':'form-control'}),
        }
