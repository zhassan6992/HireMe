from django.db import models
from client.models import Client
# from hero.models import Hero

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=300) 

    def __str__(self):
        return self.title

class HiringRequest(models.Model):
    client_id = models.ForeignKey('hero.Hero',on_delete=models.CASCADE)
    hero_id = models.ForeignKey(Client,on_delete=models.CASCADE)


class AcceptedRequest(models.Model):
    client_id = models.ForeignKey('hero.Hero',on_delete=models.CASCADE)
    hero_id = models.ForeignKey(Client,on_delete=models.CASCADE)
