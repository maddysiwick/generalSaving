from django.db import models

# Create your models here.

class Language(models.Model):
    lang=models.CharField(max_length=100)
    def __str__(self):
        return self.lang

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    languages=models.ManyToManyField(Language)
    access=models.BooleanField(default=True)
    def __str__(self):
        return self.name