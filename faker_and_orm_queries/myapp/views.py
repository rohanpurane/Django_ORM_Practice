from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .thread import *
from django.db.models import Avg, Sum, Min, Max, Count, Q
# Create your views here.
'''
Here we use faker library to generate Fake data by multithreading.
and performing some queries of ORM for interview purpose.
'''


def gen_data(request):
    count = 10
    EmployeeThread(count).start()
    return HttpResponseRedirect('/')



def home(request):
    # data = Software_Hub.objects.filter(employee_job_roll__icontains='Project Manager')
    data = Software_Hub.objects.all()
    return render(request,'home.html', {'data':data})


def operations(request):
    '''Q1)  Find Out a Employee who have Heighest Salary?'''
    # data = Software_Hub.objects.order_by('-employee_salary')[:1]
    '''Q2)  Find Out a Employee who have Second Heighest Salary?'''
    # data = Software_Hub.objects.order_by('-employee_salary')[1:2]
    '''Q3)  Find Out a Employee who have Lowest Salary?'''
    # data = Software_Hub.objects.order_by('employee_salary')[:1]
    '''Q4)  Find Out a Employee who have Second Lowest Salary?'''
    # data = Software_Hub.objects.order_by('employee_salary')[:2]
    '''Q5)  Find Out a Employee whose age is less than 45?'''
    # age = 45
    # data = Software_Hub.objects.filter(employee_age__lt=age).order_by('-employee_age')
    '''Q6)  Find Out a Employee whose age is greater than 45?'''
    # age = 45
    # data = Software_Hub.objects.filter(employee_age__gt=age).order_by('-employee_age')
    '''Q7)  Escape or skip a Employee whose age is 58?'''
    # age = 58
    # data = Software_Hub.objects.exclude(employee_age=age).order_by('-employee_age')
    # data = Software_Hub.objects.filter(~Q(employee_age=age)).order_by('-employee_age')
    '''Q8)  Find Out a Employee whose salary is 1102666 or 393533?'''
    # sal1 = 1102666
    # sal2 = 393533
    # data = Software_Hub.objects.filter(Q(employee_salary=sal1) | Q(employee_salary=sal2)).order_by('-employee_age')
    '''Q9)  Find Out a Employee whose salary is 1026173 and job-roll is Project Manager?'''
    # sal1 = 1102666
    # job_roll = 'Project Manager'
    # data = Software_Hub.objects.filter(Q(employee_salary=sal1) & Q(employee_job_roll__icontains=job_roll))
    '''Q10)  Find Out a Employee whose name starts-with {M} and Live in {Baldwin}?'''
    # starts_with = 'M'
    # live_in = 'Baldwin'
    # data = Software_Hub.objects.filter(Q(employee_name__startswith=starts_with) & Q(employee_address__icontains=live_in))
    '''Q11)  Update a Employee Salary whose Name is Martin Brown?'''
    name = 'Martin Brown'
    # new_salary = 1400000
    # Software_Hub.objects.filter(employee_name__icontains=name).update(employee_salary=new_salary)
    data = Software_Hub.objects.filter(employee_name__icontains=name)
    return render(request,'operations.html', {'data':data}) 