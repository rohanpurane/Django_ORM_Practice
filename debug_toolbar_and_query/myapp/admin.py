from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Tusion)
class TusionAdmin(admin.ModelAdmin):
    list_display = ['id','subjects']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','user','school','sub','name','city']