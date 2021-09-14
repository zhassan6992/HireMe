from django.db import models
from django.core.validators import RegexValidator
from api.models import Job
# Create your models here.

validator = RegexValidator(regex=r'^01?\d{9}$')

class Hero(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(validators=[validator],unique=True,max_length=12)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    governament = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    id_pic = models.ImageField()
    profile_pic = models.ImageField()
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name