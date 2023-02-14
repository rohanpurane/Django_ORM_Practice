from django import forms


class Filter_Data(forms.Form):
    city = forms.CharField(max_length=70)

class Number_Data(forms.Form):
    s_number = forms.IntegerField()
    e_number = forms.IntegerField()

class Q_Form(forms.Form):
    name = forms.CharField(max_length=70)
    city = forms.CharField(max_length=70)