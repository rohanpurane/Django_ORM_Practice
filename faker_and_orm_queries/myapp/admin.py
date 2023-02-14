from django.contrib import admin
from .models import *
# Register your models here.
    
@admin.register(Software_Hub)
class Software_HubAdmin(admin.ModelAdmin):
    list_display = ('employee_id','employee_name','employee_address','employee_job_roll', 'employee_salary','employee_age')