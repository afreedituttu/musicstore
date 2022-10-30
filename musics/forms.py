from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import PasswordInput

class userform(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)
    class Meta:
        model = User
        fields = ['username','password','email']