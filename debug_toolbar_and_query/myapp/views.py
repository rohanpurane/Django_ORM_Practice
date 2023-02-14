from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    form = Student.objects.all()
    return render(request, 'home.html', {'form': form})

# def home(request):
#     form = Student.objects.all().prefetch_related('user', 'school','tusion')
#     return render(request, 'home.html', {'form': form})

# def home(request):
#     form = Student.objects.all().select_related()
#     return render(request, 'home.html', {'form': form})