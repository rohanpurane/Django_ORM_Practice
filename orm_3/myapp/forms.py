from django import forms
from .models import *

class Get_Data(forms.Form):
    name = forms.CharField(max_length=70)

class Get_Int_Data(forms.Form):
    marks = forms.IntegerField()

class Get_Date_Data(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()

class Create_Data_Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name','roll','city','marks','pass_date', 'admission_date')