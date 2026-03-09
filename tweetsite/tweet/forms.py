from django import forms
from .models import Tweet
from django.contrib.auth.forms import AuthenticationForm
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
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})

class LoginForm(AuthenticationForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields["username"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"Enter username"
        })

        self.fields["password"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"Enter password"
        })