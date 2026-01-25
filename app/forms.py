from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import EmailInput, TextInput, PasswordInput
from django.contrib.auth import password_validation
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

        widgets = {'email':EmailInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Email'}),
                   'first_name':TextInput(attrs={'class':'form-control', 'required':True, 'placeholder':'First Name'}),
                   'last_name':TextInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Last Name'}),
                   'password1':PasswordInput(attrs={'class':'form-control', 'required':True, 'autocomplete':False, 'placeholder':'Password', 'help_text':password_validation.password_validators_help_text_html()}),
                   'password2':PasswordInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Password Confirmation'}),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')