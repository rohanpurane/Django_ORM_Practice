from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate
# Create your views here.


def home(request):
    form = Student.objects.all()
    return render(request, 'home.html',{'form':form})


def single_data(request):
    # form = Student.objects.order_by('name').first()
    # form = Student.objects.last()
    # form = Student.objects.latest('pass_date')
    form = Student.objects.earliest('pass_date')

    # if we want to ckech that, if a perticular data is exists or not
    # form = Student.objects.all()
    # data = Student.objects.get(city='Pune')
    # print(form.filter(city=data.city).exists())     # we can check in Terminal by True or False
    return render(request, 'single_data.html',{'fm':form})


def get_single_data(request):
    if request.method == 'POST':
        data = Get_Data(request.POST)
        if data.is_valid():
            roll = data.cleaned_data['roll']
            form = Student.objects.get(roll=roll)
            return render(request, 'get_data.html',{'fm':form})
    else:
        data = Get_Data()
    return render(request, 'get_data.html',{'data':data})


def create_data(request):
    if request.method == 'POST':
        data = Create_Data_Form(request.POST)
        if data.is_valid():
            name = data.cleaned_data['name']
            roll = data.cleaned_data['roll']
            city = data.cleaned_data['city']
            pass_date = data.cleaned_data['pass_date']
            new_data = Student.objects.create(name=name, roll=roll, city=city, pass_date=pass_date)
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