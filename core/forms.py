from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username = forms.CharField(max_length=255,widget=forms.TextInput(attrs={
            'placeholder':'Your username',
            'class':'w-full py-4 px-6 rounded-xl'
                                                                        }) )
    
    email = forms.CharField(max_length=255,widget=forms.EmailInput(attrs={
            'placeholder':'Your username',
            'class':'w-full py-4 px-6 rounded-xl'
                                                                        }) )
    
    password1 = forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={
            'placeholder':'Your password',
            'class':'w-full py-4 px-6 rounded-xl'
                                                                        }) )
    
    password2 = forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={
            'placeholder':'Confirm Your password',
            'class':'w-full py-4 px-6 rounded-xl'
                                                                        }) )

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255,widget=forms.TextInput(attrs={
            'placeholder':'Your username',
            'class':'w-full py-4 px-6 rounded-xl'
                                                                        }) )
    
    password = forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={
            'placeholder':'Your password',
            'class':'w-full py-4 px-6 rounded-xl'
                                                                        }) )
    