from app import forms
from app import models
from django.core.exceptions import ObjectDoesNotExist

#Helper class for views.py
class AuthFormHelp:
    #Create method for create session after request. If data is not valid, this method return False
    def addPostMethodForLayoutForm(self, request):
        authUserForm = forms.AuthUserForm(request.POST)
        if authUserForm.is_valid():
            try:
                account = models.Accounts.objects.get(usernameAcc=authUserForm.cleaned_data["usernameAcc"],
                                                      psswdAcc=authUserForm.cleaned_data["psswdAcc"])
                request.session["account"] = account.usernameAcc
            except ObjectDoesNotExist:
                return None
        else:
            try:
                del request.session["account"]
            except KeyError:
                return None
            return None
        return authUserForm