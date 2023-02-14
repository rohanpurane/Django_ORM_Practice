from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class School(models.Model):
    name = models.CharField(max_length=70)
    def __str__(self):
        return self.name
    

class Tusion(models.Model):
    subjects = models.CharField(max_length=70)
    def __str__(self):
        return self.subjects

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.OneToOneField(School, on_delete=models.CASCADE)
    tusion = models.ManyToManyField(Tusion)
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    def __str__(self):
        return self.name
        
    def sub(self):
        return ",".join([str(p) for p in self.tusion.all()])

