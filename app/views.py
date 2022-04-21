from django.shortcuts import render,  redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from LibraryForProject.AuthFormHelper import AuthFormHelp
from app import forms
from app import models
from .models import Vacancies
from .models import Resume
from .forms import VacancyForm
from .forms import ResumeForm

def index(request):
    vacancies = Vacancies.objects.all()
    resume = models.Resume.objects.filter(accounts=models.Accounts.objects.filter(usernameAcc=request.session.get('account', False)))

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
            "resume": resume
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
            "id_user": request.session.get("id", False),
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
            vacancy = models.Vacancies()
            vacancy.title = form.cleaned_data["title"]
            vacancy.salary = form.cleaned_data["salary"]
            vacancy.email = form.cleaned_data["email"]
            vacancy.text = form.cleaned_data["text"]
            vacancy.date = form.cleaned_data["date"]
            vacancy.imagesrs = form.cleaned_data["imagesrs"]
            vacancy.telephonenumber = form.cleaned_data["telephonenumber"]
            vacancy.complaint = 0
            vacancy.accounts = models.Accounts.objects.get(usernameAcc=request.session.get("account", False))
            vacancy.save()
            return redirect('main')
        else:
            error = 'Форма заполнена неверно'
    form = VacancyForm()
    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'app/CreateVacancy.html', data)

def CreateResume(request):

    error = ''
    if request.method == "POST":
        form = forms.ResumeForm(request.POST)
        if form.is_valid():
            resume = models.Resume()
            resume.name = form.cleaned_data["name"]
            resume.surname = form.cleaned_data["surname"]
            resume.email = form.cleaned_data["email"]
            resume.text = form.cleaned_data["text"]
            resume.date = form.cleaned_data["date"]
            resume.experience = form.cleaned_data["experience"]
            resume.imagesrs = form.cleaned_data["imagesrs"]
            resume.telephonenumber = form.cleaned_data["telephonenumber"]
            resume.complaint = 0
            resume.accounts = models.Accounts.objects.get(usernameAcc=request.session.get("account", False))
            resume.save()
            return redirect('main')
        else:
            error = 'Форма заполнена неверно'
    form = ResumeForm()
    data = {
        'form': form,
        'error': error,
        'resume': models.Resume.objects.all(),
    }

    return render(request, 'app/CreateResume.html', data)

def Resume(request, id_resume):

    if request.method == "POST":
        models.Resume.objects.filter(id=id_resume).delete()
        return HttpResponseRedirect("/")

    data = {
        'resume': models.Resume.objects.filter(id=id_resume),
        'role': request.session.get("role", False)
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
            resumes = models.Resume.objects.filter(complaint__gt=10)
            return render(
                request,
                "app/AdminPanel.html",
                {
                    "resumes": resumes
                }
            )
        elif action == "ChangeRole":
            accounts = models.Accounts.objects.all().exclude(usernameAcc=request.session.get("account", False))
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
        "app/EditRole.html",
        {
            "accName": account.usernameAcc,
            "accRole": account.roles.role_name
        }
    )