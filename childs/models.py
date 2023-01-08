from django.db import models

# Create your models here.
class Employee(models.Model):
    nationalCode = models.CharField(max_length=10, primary_key=True)
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)

    EMPLOYMENT_TYPES = [
        ('RG', 'رسمی قطعی'),
        ('RA', 'رسمی آزمایشی'),
        ('PE', 'پیمانی'),
        ('GM', 'قرارداد کارمعین'),
        ('GK', 'قرارداد کارگری'),
        ('SH', 'شرکتی')
    ]
    type_of_employment = models.CharField(
        max_length=2,
        choices=EMPLOYMENT_TYPES
        )

    EMPLOYMENT_STATUS = [
        ('SH', 'شاغل'),
        ('MO', 'مرخصی'),
        ('MA', 'مامور از'),
        ('MB', 'مامور به'),
        ('BA', 'بازنشسته')
    ]
    employment_status = models.CharField(
        max_length=2,
        choices=EMPLOYMENT_STATUS,
        default='SH'
    )

    def __str__(self):
        return self.fName + ' ' + self.lName + ' ' + self.get_employment_status_display()


#class of childs employee
class Child(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    nationalCode = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    sex = models.BooleanField()

    parent = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE
        )

    def __str__(self):
        res = '{} {} فرزند {}'.format(self.fName, self.lName, self.parent)
        return res


