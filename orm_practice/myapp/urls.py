from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('wholesale/', wholesale, name='wholesale'),
    path('retailshop/', retailshop, name='retailshop'),
]
