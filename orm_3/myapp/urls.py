from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('create_data/', create_data, name='create_data'),
    path('update_data/<slug:pk>/', update_data, name='update_data'),
    path('delete_data/<slug:pk>/', delete_data, name='delete_data'),
    path('get_lookup_data/', get_lookup_data, name='get_lookup_data'),
    path('get_int_data/', get_int_data, name='get_int_data'),
    path('get_date_data/', get_date_data, name='get_date_data'),
]
