from django.db import models
import uuid
# Create your models here.

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField(null=True, blank=True)
    pass_date = models.DateField()
    admission_date = models.DateTimeField(null=True, blank=True)