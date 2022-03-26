from django.shortcuts import render,  redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from LibraryForProject.AuthFormHelper import AuthFormHelp
from django.core import serializers
from app import forms
from app import models
from .models import Vacancies
from .models import Resume
from .forms import VacancyForm
from .forms import ResumeForm

def index(request):
    vacancies = Vacancies.objects.all()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == "GET":
            return JsonResponse({"vacancy": list(Vacancies.objects.all().values())})
        else:
            authUserForm = forms.AuthUserForm()
    else:
        if request.method == "POST":
            authUserForm = AuthFormHelp.addPostMethodForLayoutForm(request)
            if authUserForm == None:
                return HttpResponseRedirect('/')

        else:
            vacancies = Vacancies.objects.all()
            authUserForm = forms.AuthUserForm()

    return render(
        request,
        "app/index.html",
        {
            "account": request.session.get('account', False),
            "role": request.session.get("role", False),
            'vacancies': vacancies,
            "authUserForm": authUserForm,
            "statusBtnAuth": True,
        }
    )


def AboutUs(request):
    """Renders the about page."""

    if request.method == "POST":
        authUserForm = AuthFormHelp.addPostMethodForLayoutForm(request)
        if authUserForm == None:
            return HttpResponseRedirect('/about_us')
    else:
        authUserForm = forms.AuthUserForm()

    return render(
        request,

        "app/AboutUs.html",
        {
            "email": request.session.get('usernameUser', False),
            "psswd": request.session.get('psswdUser', False),
            "statusBtnAuth": True,
            "authUserForm": authUserForm,
            "persons": [{
                "person_id": "first__person",
                "name": "Leha",
                "surname": "Verstappen",
                "address": "Golubaya Ustrica",
                "email": "nenaebnaden'gi@com",
                "telephone": '8-800-353-55-55'
            },
                {
                    "person_id": "second__person",
                    "name": "Doner",
                    "surname": "Hamilton",
                    "adress": "Psihushka d2",
                    "email": "300$@com",
                    "telephone": "8-800-555-35-35"

                }]
        }
    )

def Vacancy(request, id_vacancy):
    vacancies = Vacancies.objects.filter(id=id_vacancy)
    data = {"something": id_vacancy, "authUserForm": forms.AuthUserForm, 'vacancies': vacancies}
    return render(
            request,
            "app/Vacancy.html",
            context=data
        )


def Registration(request):
    if request.method == "POST":
        regForm = forms.RegistrationForm(request.POST)
        if regForm.is_valid():
           try:
               user = models.Accounts.objects.get(usernameAcc=request.POST.get("reg_username", False))
               return render(
                   request,
                   "app/registrationPage.html",
                   {
                       "regForm": regForm,
                       "errors": "This username exist, let's create new username",
                   }
               )
           except ObjectDoesNotExist:
               psswd, chk_psswd = regForm.cleaned_data["reg_psswd"], regForm.cleaned_data["reg_chkpsswd"]
               if psswd == chk_psswd:
                   account = models.Accounts()
                   account.usernameAcc = regForm.cleaned_data["reg_username"]
                   account.psswdAcc = psswd
                   account.emailAcc = regForm.cleaned_data["reg_email"]
                   account.roles = models.Roles(id=regForm.cleaned_data["regUserCompChoice"])
                   account.save()
                   return HttpResponseRedirect('/')
               else:
                   return render(
                       request,
                       "app/RegistrationPage.html",
                       {
                           "regForm": regForm,
                           "errors": "Passwords don't match",
                       }
                   )
        else:
            return render(
                request,
                "app/RegistrationPage.html",
                {
                    "regForm": regForm,
                    "errors": "Your data is not valid. Please rewrite that form!",
                }
            )

    else:
        regForm = forms.RegistrationForm()

    return render(
        request,
        "app/RegistrationPage.html",
        {
            "regForm": regForm,
            "errors": False,
        }
    )

def CreateVacancy(request):
    error = ''

    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Форма заполнена неверно'
    form = VacancyForm()
    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'app/CreateVacancy.html', data)

resume = Resume.objects.all()
def CreateResume(request):

    error = ''
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Форма заполнена неверно'
    form = ResumeForm()
    data = {
        'form': form,
        'error': error,
        'resume': resume,
    }

    return render(request, 'app/CreateResume.html', data)

def Resume(request):

    data = {
        'resume': resume,
    }

    return render(request, 'app/Resume.html', data)

def Search(request):
    return render(
        request,
        'app/Search.html',
    )

def AdminPanel(request, action):
    if request.session.get("role", False) and request.session.get("role", False) == "admin":
        if action == "CheckComplaint":
            return render(
                request,
                "app/AdminPanel.html",
                {

                }
            )
        elif action == "ChangeRole":
            accounts = models.Accounts.objects.all()
            return render(
                request,
                "app/AdminPanel.html",
                {
                    "accounts": accounts
                }
            )
    return HttpResponseRedirect("/")

def EditRole(request, acc_id):
    try:
        account = models.Accounts.objects.get(id=acc_id)
        if request.method == "POST":
            choice = request.POST.get("role")
            role = None

            if choice == '1':
                role = models.Roles.objects.get(role_name="user")
            if choice == '2':
                role = models.Roles.objects.get(role_name="company")
            if choice == '3':
                role = models.Roles.objects.get(role_name="admin")

            account.roles_id = role.id
            account.save()
            return HttpResponseRedirect("/adminPanel/ChangeRole")


    except ObjectDoesNotExist:
        return HttpResponseRedirect("/")

    return render(
        request,
        "app/EditRole.html"
    )