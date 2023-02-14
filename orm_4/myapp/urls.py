from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('create_data/', create_data, name='create_data'),
    path('update_data/<slug:pk>/', update_data, name='update_data'),
    path('delete_data/<slug:pk>/', delete_data, name='delete_data'),
    path('q_object/', q_object, name='q_object'),
]
