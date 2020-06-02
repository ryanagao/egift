from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect, get_object_or_404, render_to_response

from . import models
from django.contrib.auth.forms import UserChangeForm

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255, label='',
        widget=forms.EmailInput(
            attrs={'class': 'marg-t-20', 'placeholder': 'Email'}
        ))
    password = forms.CharField(max_length=255, label='',
        widget=forms.PasswordInput(
            attrs={'class': 'marg-t-20', 'placeholder': 'Password'}
        ))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Incorrect username or password')
            if not user.is_active:
                raise forms.ValidationError('User is not active')
        return super(LoginForm, self).clean(*args, **kwargs)


class MerchantSignupForm(forms.Form):
    company_name = forms.CharField(max_length=255, label='',
        widget=forms.TextInput(
            attrs={'class': 'marg-t-20', 'placeholder': 'Business/Company Name'}
        ))
    email = forms.EmailField(max_length=255, label='',
        widget=forms.EmailInput(
            attrs={'class': 'marg-t-20', 'placeholder': 'Email'}
        ))
    contact_person = forms.CharField(max_length=255, label='',
        widget=forms.TextInput(
            attrs={'class': 'marg-t-20', 'placeholder': 'Main Contact Person'}
        ))
    contact_no = forms.CharField(max_length=64, label='',
        widget=forms.TextInput(
            attrs={'class': 'marg-t-20', 'placeholder': 'Contact Number'}
        ))
    address = forms.CharField(max_length=255, label='',
        widget=forms.TextInput(
            attrs={'class': 'marg-t-20', 'placeholder': 'Company Address'}
        ))
    description = forms.CharField(max_length=255, label='',
        widget=forms.TextInput(
            attrs={'class': 'marg-t-20', 'placeholder': 'Tell us a little about your business/company'}
        ))


    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_queryset = models.User.objects.filter(email=email)
        if email_queryset.exists():
            raise forms.ValidationError('Email already used')

        return email


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(max_length=255,
                widget=forms.EmailInput(
                    attrs={'id': 'profile-name',
                        'class': 'form-control',
                        'aria-required': 'true',
                    }))
    class Meta:
        model = models.Profile
        fields = [
            'name',
            'description',
            'tel_no',
            'address',
            'terms_and_condition',
            'logo',
            'logo_banner',
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'profile-name',
                    'class': 'form-control',
                    'aria-required': 'true',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'id': 'profile-name',
                    'class': 'form-control',
                    'aria-required': 'true',
                    'rows': 6,
                    'aria-invalid': "false"
                }
            ),
            'tel_no': forms.TextInput(
                attrs={
                    'id': 'profile-name',
                    'class': 'form-control',
                    'aria-required': 'true',
                }
            ),
            'address': forms.Textarea(
                attrs={
                    'id': 'profile-name',
                    'class': 'form-control',
                    'aria-required': 'true',
                    'rows': 6,
                    'aria-invalid': "false"
                }
            ),
            'terms_and_condition': forms.Textarea(
                attrs={
                    'id': 'profile-name',
                    'class': 'form-control',
                    'aria-required': 'true',
                    'rows': 6,
                    'aria-invalid': "false"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(ProfileForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        email = cleaned_data.get('email')
        email_exist = models.User.objects.filter(
            email=email).exclude(
            id=self.request.user.pk).exists()

        if email_exist:
            raise forms.ValidationError(
                'Email "'+email+'" has already been taken'
            )


class CredentialForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={'id': 'user-username','class': 'form-control', 'aria-required': 'true'}
        ))
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(
            attrs={'id': 'user-email','class': 'form-control', 'aria-required': 'true'}
        ))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
            attrs={'id': 'user-password','class': 'form-control', 'aria-required': 'true'}
        ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
            attrs={'id': 'user-password_repeat','class': 'form-control', 'aria-required': 'true'}
        ))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(CredentialForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CredentialForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        email_exist = models.User.objects.filter(
            email=cleaned_data.get('email')).exclude(
            id=self.request.user.pk).exists()

        if email_exist:
            raise forms.ValidationError(
                "email already used"
            )

        if password != confirm_password:
            raise forms.ValidationError(
                "password not matched"
            )