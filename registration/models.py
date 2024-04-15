from django.db import models
class student(models.Model):
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     date_of_birth = models.DateField()
     email = models.EmailField(unique=True)
     phone_number = models.CharField(max_length=15, blank=True, null=True)
     address = models.CharField(blank=True, null=True , max_length=100)


class registerstudents(models.Model):
      first_name = models.CharField(max_length=100)
      last_name = models.CharField(max_length=100)
      email = models.EmailField(unique=True)
      phone_number = models.CharField(max_length=15, blank=True, null=True)
      age= models.IntegerField(blank=True, null=True)









#models are python classes that help you create tables which store your work in the databases
#the database is an electronic way of storing data in your computer
#we use migrations to keep track of wat happens in the models.py to update delete  and add items pytho
# Create your models here.
