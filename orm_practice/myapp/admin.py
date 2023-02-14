from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(WholeSaleShop)
class WholeSaleShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'w_name', 'w_qty')
    
@admin.register(RetailShop)
class RetailShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'r_name', 'r_qty')
    