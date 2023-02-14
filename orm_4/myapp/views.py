from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Avg, Sum, Min, Max, Count, Q
# Create your views here.

def home(request):
    form = Student.objects.all()
    average = form.aggregate(Avg('marks'))
    total = form.aggregate(Sum('marks'))
    count = form.aggregate(Count('marks'))
    minimum = form.aggregate(Min('marks'))
    maximum = form.aggregate(Max('marks'))
    context = {
        'form':form,
        'average':average,
        'total':total,
        'count':count,
        'minimum':minimum,
        'maximum':maximum,
    }
    return render(request, 'home.html',context)

def q_object(request):
    # data = Student.objects.filter(Q(name='Suresh') & Q(city='Beed'))
    data = Student.objects.filter(Q(name='Mahesh') | Q(city='Beed'))
    # data = Student.objects.filter(~Q(city='Beed'))
    return render(request, 'Q_data.html',{'data':data})



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
