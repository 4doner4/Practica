from django.db import models

class Vacancies(models.Model):
    title = models.CharField('Name', max_length= 50)
    salary = models.CharField('Salary', max_length=20)
    email = models.CharField('Email', max_length=50)
    text = models.TextField('Text')
    date = models.DateField('Data')
    Imagesrs = models.CharField('Imageurl', max_length=50)
    Telephonenumber = models.CharField('Telephonenumber', max_length=20)
    def __str__(self):
        return self.title
