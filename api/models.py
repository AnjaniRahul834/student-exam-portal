from email.headerregistry import Address
from django.db import models



# Create your models here.


class Task(models.Model):
    Name = models.CharField(max_length=200)
    Section = models.IntegerField()
    Address = models.CharField(max_length=400)
    Contact = models.IntegerField()
    Email = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

   
