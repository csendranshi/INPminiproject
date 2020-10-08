from django import forms

from .models import *


class PersonalDetails(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'auth-form-input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'auth-form-input'}))
    email_id = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email ID', 'class': 'auth-form-input'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'auth-form-input'}))
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'Date of Birth', 'class': 'auth-form-input'}))

    class Meta:
        model = PersonalDetails
        fields = '__all__'
