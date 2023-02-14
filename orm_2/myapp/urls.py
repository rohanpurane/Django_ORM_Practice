from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('single_data/', single_data, name='single_data'),
    path('get_single_data/', get_single_data, name='get_single_data'),
    path('create_data/', create_data, name='create_data'),
    path('update_data/<slug:pk>/', update_data, name='update_data'),
    path('delete_data/<slug:pk>/', delete_data, name='delete_data'),
]
