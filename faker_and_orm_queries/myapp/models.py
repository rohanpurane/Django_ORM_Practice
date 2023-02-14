from django.db import models
import uuid
# Create your models here.

# class Client(models.Model):
#     company_name = models.CharField(max_length=100)
#     company_email = models.EmailField(max_length=100)
#     company_phone = models.BigIntegerField()
#     company_info = models.TextField()


class Software_Hub(models.Model):
    employee_id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    employee_name = models.CharField(max_length=100)
    employee_address = models.CharField(max_length=100)
    employee_job_roll = models.CharField(max_length=100)
    employee_salary = models.IntegerField()
    employee_age = models.IntegerField()

    def __str__(self):
        return self.employee_name

# class Services(models.Model):
    