from django import forms
from .models import Vacancies
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class AuthUserForm(forms.Form):
    email = forms.EmailField(label="Email:", help_text="You need to add '@example.com' at the end", widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    psswd = forms.CharField(label="Password:", widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))

class RegistrationUserForm(forms.Form):
    name = forms.CharField(label="Your name:", widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    reg_email = forms.EmailField(label="Your email:", widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    reg_psswd = forms.CharField(label="Your password:", widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))
    chk_psswd = forms.CharField(label="Repeat password:", widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))

class VacancyForm(ModelForm):
    class Meta:
        model = Vacancies
        fields = ['title', 'salary', 'email', 'text', 'date', 'Imagesrs', 'Telephonenumber']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название вакансии'
            }),
            "salary": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Зарплата'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email аддрес'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст вакансии'
            }),
            "Imagesrs": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на изображения'
            }),
            "Telephonenumber": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
        }