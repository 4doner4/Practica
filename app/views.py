from django.shortcuts import render,  redirect
from django.http import HttpResponseRedirect
from app import forms
from .models import Vacancies
from .models import Resume
from .forms import VacancyForm
from .forms import ResumeForm

def index(request):
    vacancies = Vacancies.objects.all()


    if request.method == "POST":
        authUserForm = forms.AuthUserForm(request.POST)
        if authUserForm.is_valid():
            request.session['emailUser'] = authUserForm.cleaned_data["email"]
            request.session['psswdUser'] = authUserForm.cleaned_data["psswd"]
        else:
            try:
                del request.session['emailUser']
                del request.session['psswdUser']
            except KeyError:
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('/')


    else:
        authUserForm = forms.AuthUserForm()

    return render(
        request,
        "app/index.html",
        {"email": request.session.get('emailUser', False),
         "psswd": request.session.get('psswdUser', False),
         "statusBtnAuth": True,
         'vacancies': vacancies,
         "authUserForm": authUserForm},

    )

def TeamMembers(request):
    names = ["Leha", "Doner"]
    surnames = ["Verstapen", "Hemelton"]
    data = {"names" : names, "surnames": surnames, "authUserForm": forms.AuthUserForm}
    return render(
        request,
        "app/TeamMembersPage.html",
        context = data
    )

def ProjectInformation(request):
    data = {"authUserForm": forms.AuthUserForm}
    return render(
        request,
        "app/ProjectInformationPage.html",
        context=data
    )

def TeamInfo(request):
    data = {"authUserForm": forms.AuthUserForm}
    return render(
        request,
        "app/TeamInformationPage.html",
        context=data
    )

def AboutUs(request):
    """Renders the about page."""

    return render(
        request,
        'app/AboutUs.html',
        {

        }
    )

def Vacancy(request, id_vacancy):
    data = {"something": id_vacancy, "authUserForm": forms.AuthUserForm}
    return render(
        request,
        "app/Vacancy.html",
        context=data
    )

def Registration(request, type_registration):
    if request.method == "POST":
        regUserForm = forms.RegistrationUserForm(request.POST)

        if regUserForm.is_valid():
            i = 1
        else:
            i = 2
    else:
        regUserForm = forms.RegistrationUserForm()

    return render(
        request,
        "app/RegistrationPage.html",
        {
        "statusBtnAuth": False,
        "regUserForm": regUserForm,
        "type_registration": type_registration}
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
        'error': error
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
        'resume': resume
    }

    return render(request, 'app/CreateResume.html', data)
def Resume(request):
    data = {
        'resume': resume
    }

    return render(request, 'app/CreateResume.html', data)