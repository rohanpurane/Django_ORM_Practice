from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('gen_data/',gen_data, name='gen_data'),
    path('operations/',operations, name='operations'),
]
