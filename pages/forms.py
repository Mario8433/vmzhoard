from django import forms

class EditTextForm(forms.Form):
    originalText = forms.CharField(label="Text",widget=forms.Textarea)

class SignUpForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")
    email = forms.CharField(label="Email")
    first_name = forms.CharField(label="First Name",required=False)
    last_name = forms.CharField(label="Last Name",required=False)

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")