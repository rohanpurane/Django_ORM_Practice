from django.shortcuts import render, redirect
from .models import *
from. forms import *
from django.db.models import Q
# Create your views here.

def home(request):
    form = Student.objects.all()

    # if we want to show specific column ---->it show data in dictionary
    # form = Student.objects.values()
    # form = Student.objects.values('id','name','roll')
    
    # if we want to show specific column ---->it show data in tuple
    # form = Student.objects.values_list(named=True)
    # form = Student.objects.values_list('id','name','roll', named=True)

    # if we want to show data in such order
    # form = Student.objects.order_by('city')
    # form = Student.objects.order_by('-city')
    # form = Student.objects.order_by('?')
    # form = Student.objects.order_by('roll').reverse()

    # if we have more than one database and if we want to use specific database
    # form = Student.objects.using('default') # ow we are using default then mention 'default' but if we deffernt database then mention name of database
    return render(request, 'home.html',{'form':form})


def filter_operation(request):
    if request.method == 'POST':
        data = Filter_Data(request.POST)
        if data.is_valid():
            city = data.cleaned_data['city']
            form = Student.objects.filter(city__icontains=city)
            return render(request, 'filter.html',{'form':form})
    else:
        data = Filter_Data()
    return render(request, 'filter.html',{'data':data})

def exclude_operation(request):
    if request.method == 'POST':
        data = Filter_Data(request.POST)
        if data.is_valid():
            city = data.cleaned_data['city']
            form = Student.objects.exclude(city__icontains=city)
            return render(request, 'exclude.html',{'form':form})
    else:
        data = Filter_Data()
    return render(request, 'exclude.html',{'data':data})

def some_no_of_data(request):
    if request.method == 'POST':
        data = Number_Data(request.POST)
        if data.is_valid():
            s_number = data.cleaned_data['s_number']
            e_number = data.cleaned_data['e_number']
            form = Student.objects.all()[s_number:e_number]
            return render(request, 'number_data.html',{'form':form})
    else:
        data = Number_Data()
    return render(request, 'number_data.html',{'data':data})


def Q_operation(request):
    if request.method == 'POST':
        data = Q_Form(request.POST)
        if data.is_valid():
            name = data.cleaned_data['name']
            city = data.cleaned_data['city']
            # form = Student.objects.filter(Q(city__icontains=city) & Q(name__icontains=name))
            form = Student.objects.filter(Q(city__icontains=city) | Q(name__icontains=name))
            return render(request, 'Q_operations.html',{'form':form})
    else:
        data = Q_Form()
    return render(request, 'Q_operations.html',{'data':data})



###### Some Queries ######

# (1) select_related(*fields)
# (2) defer(*fields)
# (3) only(*fields)
# (4) prefetch_related(*lookups)
# (5) raw()
# (6) annotate(*args, **kwargs)
# (7) select_for_update(nowait=False, skip_locked=False, of=())
# (8) extra()