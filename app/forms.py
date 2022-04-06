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

class VacancyForm(forms.Form):
    title = forms.CharField(label="Название вакансии",
                            widget=forms.TextInput(attrs={"class": "form-control fromsvacancy", "placeholder": "Название вакансии"}))
    salary = forms.CharField(label="Зарплата",
                             widget=forms.TextInput(attrs={"class": "form-control fromsvacancy", "placeholder": "Размер зарплаты"}))
    email = forms.EmailField(label="Email",
                             widget=forms.TextInput(attrs={"class": "form-control fromsvacancy", "placeholder": "Ваш email"}))
    text = forms.CharField(label="Описание вакансии",
                           widget=forms.Textarea(attrs={"class": "form-control fromsvacancy", "placeholder": "Описание"}))
    date = forms.DateField(label="Дата публикации",
                           widget=forms.DateInput(attrs={"class": "form-control fromsvacancy", "placeholder": "Дата публикации"}))
    imagesrs = forms.CharField(label="Ссылка на фото",
                              widget=forms.TextInput(attrs={"class": "form-control fromsvacancy", "placeholder": "Путь к файлу"}))
    telephonenumber = forms.CharField(label="Номер телефона",
                                      widget=forms.TextInput(attrs={"class": "form-control fromsvacancy", "placeholder": "Номер телефона"}))

class ResumeForm(forms.Form):
    name = forms.CharField(label="Имя",
                           widget=forms.TextInput(attrs={"class": "form-control fromsvacancy", "placeholder": "Имя"}))
    surname = forms.CharField(label="Фамилия",
                              widget=forms.TextInput(attrs={"class": "form-control fromsvacancy", "placeholder": "Фамилия"}))
    email = forms.EmailField(label="Email",
                             widget=forms.TextInput(attrs={"class": "form-control fromsvacancy", "placeholder": "Email"}))
    text = forms.CharField(label="Текст",
                           widget=forms.Textarea(attrs={"class": "form-control fromsvacancy", "placeholder": "Ваш текст"}))
    date = forms.DateField(label="Ваша дата:",
                           widget=forms.DateInput(attrs={"class": "form-control fromsvacancy", "placeholder": "Дата рождения"}))
    experience = forms.CharField(label="Опыт работы:",
                                 widget=forms.TextInput(attrs={"class": "form-control fromsvacancy", "placeholder": "Опыт работы"}))
    imagesrs = forms.CharField(label="Ссылка на фотографию:",
                               widget=forms.TextInput(attrs={"class": "form-control fromsvacancy", "placeholder": "Ссылка на фото"}))
    telephonenumber = forms.CharField(label="Номер телефона:",
                                      widget=forms.TextInput(attrs={"class": "form-control fromsvacancy", "placeholder": "Номер телефона"}))