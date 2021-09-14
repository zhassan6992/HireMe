from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

validator = RegexValidator(regex=r'^01?\d{9}$')
class Client(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(validators=[validator],unique=True,max_length=12)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    governament = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    profile_pic = models.ImageField()

    def __str__(self):
        return self.name
    