from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, initial='@dartmouth.edu', help_text='Only emails from dartmouths domain will be accepted as valid')
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)


    def clean_email(self):
        submitted_data = self.cleaned_data['email'].lower()
        if '@dartmouth.edu' not in submitted_data:
            raise forms.ValidationError('You must register using a Dartmouth address')
        return submitted_data

    class Meta:
        model = User
        fields=['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
