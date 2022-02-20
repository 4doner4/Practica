from django import forms

class AuthUserForm(forms.Form):
    email = forms.EmailField(label="Email:", help_text="You need to add '@example.com' at the end", widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    psswd = forms.CharField(label="Password:", widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))

class RegistrationUserForm(forms.Form):
    name = forms.CharField(label="Your name:", widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    reg_email = forms.EmailField(label="Your email:", widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    reg_psswd = forms.CharField(label="Your password:", widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))
    chk_psswd = forms.CharField(label="Repeat password:", widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))
