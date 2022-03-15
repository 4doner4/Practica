from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="main"),
    path('vacancy/<str:id_vacancy>', views.Vacancy, name="vacancy"),
    path('registration/', views.Registration, name='registration'),
    path('about_us/', views.AboutUs, name="AboutUs"),
    path('CreateVacancy', views.CreateVacancy, name="CreateVacancy"),
    path('CreateResume', views.CreateResume, name="CreateResume"),
    path('Resume', views.Resume, name="Resume"),
    path('Search', views.Search, name="Search"),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
