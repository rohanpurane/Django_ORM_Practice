from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.


def home(request):
    form = Student.objects.all()
    return render(request, 'home.html',{'form':form})



def create_data(request):
    if request.method == 'POST':
        data = Create_Data_Form(request.POST)
        if data.is_valid():
            name = data.cleaned_data['name']
            roll = data.cleaned_data['roll']
            city = data.cleaned_data['city']
            marks = data.cleaned_data['marks']
            pass_date = data.cleaned_data['pass_date']
            admission_date = data.cleaned_data['admission_date']
            new_data = Student.objects.create(name=name, roll=roll, city=city, marks=marks, pass_date=pass_date,admission_date=admission_date)
            # get_or_create(), bulk_create()
            return render(request, 'create_data.html',{'fm':new_data})
    else:
        data = Create_Data_Form()
    return render(request, 'create_data.html',{'data':data})


# (1) update_data   = update(), update_or_create()
def update_data(request,pk):
    if request.method == 'POST':
        pi = Student.objects.get(pk=pk)
        form = Create_Data_Form(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        pi = Student.objects.get(pk=pk)
        form = Create_Data_Form(instance=pi)
    return render(request,'update_data.html',{'form':form})


def delete_data(request,pk):
    if request.method == 'POST':
        content = Student.objects.get(pk=pk)
        content.delete()
    return redirect('home')

def get_lookup_data(request):
    if request.method == 'POST':
        form = Get_Data(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # data = Student.objects.filter(name__exact=name)
            # data = Student.objects.filter(name__iexact=name)
            # data = Student.objects.filter(name__contains=name)
            # data = Student.objects.filter(name__icontains=name)
            # data = Student.objects.filter(name__in=['Mukesh','Gautam','Sonali'])
            # data = Student.objects.filter(name__in=[name])
            # data = Student.objects.filter(name__startswith=name)
            # data = Student.objects.filter(name__istartswith=name)
            # data = Student.objects.filter(name__endswith=name)
            # data = Student.objects.filter(name__iendswith=name)
            data = Student.objects.filter(name__iendswith=name)
            return render(request,'get_data.html',{'data':data})
    else:
        form = Get_Data()
    return render(request,'get_data.html',{'form':form})

def get_int_data(request):
    if request.method == 'POST':
        form = Get_Int_Data(request.POST)
        if form.is_valid():
            marks = form.cleaned_data['marks']
            # data = Student.objects.filter(marks__gt=marks)
            # data = Student.objects.filter(marks__gte=marks)
            # data = Student.objects.filter(marks__lt=marks)
            data = Student.objects.filter(marks__lte=marks)
            return render(request,'int_data.html',{'data':data})
    else:
        form = Get_Int_Data()
    return render(request,'int_data.html',{'form':form})

def get_date_data(request):
    if request.method == 'POST':
        form = Get_Date_Data(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            data = Student.objects.filter(pass_date__range=(start_date,end_date))
            return render(request,'date_filter.html',{'data':data})
    else:
        form = Get_Date_Data()
    return render(request,'date_filter.html',{'form':form})

