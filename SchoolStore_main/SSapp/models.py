from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.department)

class Courses(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    course = models.CharField(max_length=200)
    def __str__(self):
        return self.course

class Purposes(models.Model):
    purpose = models.CharField(max_length=200)
    def __str__(self):
        return self.purpose

class StudentForm(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(default="1996-09-3")
    s_gender=(('male',"Male"),('female',"Female"),('trans',"Trans"))
    gender = models.CharField(max_length=25,choices=s_gender)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    mail = models.EmailField(max_length=100)
    address = models.CharField(max_length=250)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,blank=True,null=True)
    course = models.ForeignKey(Courses,on_delete=models.SET_NULL,blank=True,null=True)
    purpose = models.ForeignKey(Purposes,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return '{}'.format(self.name)
class Review(models.Model):
    name = models.CharField(max_length=200)
    review = models.TextField(blank=True)

    def __str__(self):
        return self.review

