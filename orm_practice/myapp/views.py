from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate
# Create your views here.

def home(request):
    form = WholeSaleShop.objects.all()
    return render(request, 'home.html', {'form':form})

def wholesale(request):
    if request.method == 'POST':
        form = WholeSaleShopForm(request.POST)
        if form.is_valid():
            w_name = form.cleaned_data['w_name']
            w_qty = form.cleaned_data['w_qty']
            WholeSaleShop.objects.create(w_name=w_name, w_qty=w_qty)
            return redirect('wholesale')
    else:
        form = WholeSaleShopForm()
    return render(request, 'wholesale.html', {'form':form})

def retailshop(request):
    if request.method == 'POST':
        form = RetailShopForm(request.POST)
        if form.is_valid():
            r_name = form.cleaned_data['r_name']
            r_qty = form.cleaned_data['r_qty']
            if WholeSaleShop.objects.filter(w_name__icontains=r_name).exists():
                if not RetailShop.objects.filter(r_name__icontains=r_name).exists():
                    am = WholeSaleShop.objects.get(w_name__icontains=r_name)
                    if am.w_qty >= r_qty:
                        am.w_qty = am.w_qty - r_qty
                        am.save()
                        RetailShop.objects.create(r_name=r_name, r_qty=r_qty)
                        return redirect('retailshop')
                elif RetailShop.objects.filter(r_name__icontains=r_name).exists():
                    am = WholeSaleShop.objects.get(w_name__icontains=r_name)
                    pm = RetailShop.objects.get(r_name__icontains=r_name)
                    if am.w_qty >= r_qty:
                        am.w_qty -= r_qty
                        am.save()
                        pm.r_qty += r_qty
                        pm.save()
                        return redirect('retailshop')
                else:
                    return redirect('home')
            
            return redirect('retailshop')
    else:
        form = RetailShopForm()
    return render(request, 'retailshop.html', {'form':form})
