from django.db import models

# Create your models here.
class Person(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    directPhone = models.CharField(max_length=8, blank=True, verbose_name='مستقیم')
    internalPhone = models.CharField(max_length=3, blank=True, verbose_name='داخلی')
    mobilePhone = models.CharField(max_length=11, blank=True, verbose_name='همراه')
    email = models.EmailField(max_length=254, blank=True, verbose_name='پست الکترونیک')

    def __str__(self):
        return self.fName + ' ' + self.lName