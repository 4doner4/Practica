from django.contrib import admin
from app import models
# Register your models here.
from .models import Vacancies
from .models import Resume

admin.site.register(Vacancies)
admin.site.register(Resume)

admin.site.register(models.Accounts)
admin.site.register(models.Roles)