from django.db import models
from django.db.models import Model
from datetime import date, datetime


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=250)
    priority = models.IntegerField()
    date=models.DateField(default=datetime.now)
    def __str__(self):
        return self.name
