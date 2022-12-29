from django.db import models

# Create your models here.
class Person(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    directPhone = models.CharField(max_length=8)
    internalPhone = models.CharField(max_length=3)
    mobilePhone = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)