from django import forms
from .models import *

class Get_Data(forms.Form):
    roll = forms.CharField(max_length=70)

class Create_Data_Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name','roll','city','pass_date')