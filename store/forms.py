from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Comment, Movie, Rating

class SignUpForm(UserCreationForm):
  password1 = forms.CharField(label='Password', widget=forms.
                              PasswordInput(attrs={'class':'form-control'}))
  password2 = forms.CharField(label='Confirm password', widget=forms.
                              PasswordInput(attrs={'class':'form-control'}))
  
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    labels = {'username':'Username', 'first_name':'First name',
              'last_name':'Last name', 'email':'E-mail'}
    
    widgets = {
      'username': forms.TextInput(attrs={'class':'form-control'}),
      'first_name': forms.TextInput(attrs={'class':'form-control'}),
      'last_name': forms.TextInput(attrs={'class':'form-control'}),
      'email': forms.EmailInput(attrs={'class':'form-control'}),
    }
  

class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
  password = forms.CharField(
    label=_("Password"), strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )


class MovieForm(forms.ModelForm):
  class Meta:
    model = Movie 
    fields = ('user', 'director', 'title', 'poster', 'synopsis', 'year')
  

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('user', 'text')

    widgets = {
      'user': forms.TextInput(attrs= {
        'class': 'user-input',
        'style': 'color: black; font-size: 15px',
      }),
      'text':forms.Textarea(attrs= {
        'class': 'text-input',
        'style': 'color: black; font-size: 15px'
      }),
    }


class RatingForm(forms.ModelForm):
  class Meta:
    model = Rating
    fields = ('rate',)
