from django import forms

class CreateTextForm(forms.Form):
    originalText = forms.CharField(label="Text")

class SignUpForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")
    email = forms.CharField(label="Email")
    first_name = forms.CharField(label="First Name",required=False)
    last_name = forms.CharField(label="Last Name",required=False)

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")