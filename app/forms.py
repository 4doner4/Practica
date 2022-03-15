from django import forms
from .models import Vacancies
from .models import Resume
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from app import models
from django import forms

class AuthUserForm(ModelForm):
    class Meta:
        model = models.Accounts
        fields = ['usernameAcc', 'psswdAcc']
        widgets = {
            'usernameAcc': forms.TextInput(attrs={"class": "form-control form-auth__input"}),
            'psswdAcc': forms.PasswordInput(attrs={"class": "form-control form-auth__input"})
        }
#Register Form for Users
class RegistrationForm(forms.Form):
    reg_username = forms.CharField(label="Your username:",
                                   help_text="Please write username for this site",
                                   widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    reg_email = forms.EmailField(label="Your email:",
                                 help_text="Please, add the part '@example.com'",
                                 widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    reg_psswd = forms.CharField(label="Your password:",
                                help_text="Please write a password for your account",
                                widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))
    reg_chkpsswd = forms.CharField(label="Repeat your password:",
                                   help_text="Please, write password again and don't forget!",
                                   widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))
    regUserCompChoice = forms.ChoiceField(label="Who do you want to register?",
                                          choices=[(1, "User"), (2, "Company")],
                                          widget=forms.RadioSelect(attrs={"class": "form-check-input form-auth__input"}))

class SearchForm(forms.Form):
    search_inp = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control mr-sm-0"}))


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancies
        fields = ['title', 'salary', 'email', 'text', 'date', 'Imagesrs', 'Telephonenumber']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Название вакансии'
            }),
            "salary": TextInput(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Зарплата'
            }),
            "email": TextInput(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Email аддрес'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Дата публикации'
            }),
            "text": Textarea(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Текст вакансии'
            }),
            "Imagesrs": TextInput(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Ссылка на изображения'
            }),
            "Telephonenumber": TextInput(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Телефон'
            }),
        }
class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'surname', 'email', 'text', 'date', 'experience', 'Imagesrs', 'Telephonenumber']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Имя'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Фамилия'
            }),
            "email": TextInput(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Email аддрес'
            }),
            "experience": TextInput(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Опыт работы'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Дата публикации'
            }),
            "text": Textarea(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Информация о себе'
            }),
            "Imagesrs": TextInput(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Ссылка на изображения'
            }),
            "Telephonenumber": TextInput(attrs={
                'class': 'form-control fromsvacancy',
                'placeholder': 'Телефон'
            }),
        }