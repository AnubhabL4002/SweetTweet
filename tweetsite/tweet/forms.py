from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    text = forms.CharField(
        max_length=280,
        widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 40,
            'maxlength': 280,
            'placeholder': 'Write your tweet here...',
        })
    )
    
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')