from django.db import models

class Roles(models.Model):
    role_name = models.CharField('Roles Name', max_length=100)

    def __str__(self):
        return self.role_name

class Accounts(models.Model):
    usernameAcc = models.CharField('Username', max_length=100)
    psswdAcc = models.CharField('Password', max_length=100)
    emailAcc = models.EmailField('Email', max_length=200)
    telephoneAcc = models.CharField('Telephone', max_length=100, null=True, blank=True)
    aboutCompAcc = models.CharField('About company', max_length=1000, null=True, blank=True)
    logoCompAcc = models.ImageField('Image', upload_to="companies_photo/", null=True, blank=True)
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return self.usernameAcc

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

