from django.db import models

class Vacancies(models.Model):
    title = models.CharField('title', max_length= 50)
    salary = models.CharField('Salary', max_length=20)
    email = models.CharField('Email', max_length=50)
    text = models.TextField('Text')
    date = models.DateField('Data')
    Imagesrs = models.CharField('Imageurl', max_length=50)
    Telephonenumber = models.CharField('Telephonenumber', max_length=20)
    def __str__(self):
        return self.title

class Resume(models.Model):
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    email = models.CharField('Email', max_length=50)
    text = models.TextField('Text')
    date = models.DateField('Data')
    experience = models.CharField("Experience", max_length= 100)
    Imagesrs = models.CharField('Imageurl', max_length=50)
    Telephonenumber = models.CharField('Telephonenumber', max_length=20)
    def __str__(self):
        return self.name