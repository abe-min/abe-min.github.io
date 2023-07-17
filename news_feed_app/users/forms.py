from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile


class RegisterForm(UserCreationForm):

    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    #email = forms.EmailField(required=True,
    #                         widget=forms.TextInput(attrs={'placeholder': 'Email',
    #                                                       'class': 'form-control',
    #                                                       }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    #remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password']



#Here we extend the Django built in User model to include a profile or settings attribute, that way each user will have a set of settings attached to them
class UpdateProfileForm(forms.ModelForm):
    General = forms.BooleanField(required=True)
    Business = forms.BooleanField(required=False)
    Entertainment = forms.BooleanField(required=False)
    Health = forms.BooleanField(required=False)
    Science = forms.BooleanField(required=False)
    Sports = forms.BooleanField(required=False)
    Technology = forms.BooleanField(required=False)

    class Meta:
        model = Profile
        fields = ['General', 'Business', 'Entertainment', 'Health', 'Science', 'Sports', 'Technology']
