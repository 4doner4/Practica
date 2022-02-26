from django.contrib import admin

# Register your models here.
from .models import Vacancies
from .models import Resume
admin.site.register(Vacancies)
admin.site.register(Resume)
