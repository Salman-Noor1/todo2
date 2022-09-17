from turtle import title
from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=250)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title