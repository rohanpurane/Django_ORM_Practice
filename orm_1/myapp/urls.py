from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('filter_operation/', filter_operation, name='filter_operation'),
    path('exclude_operation/', exclude_operation, name='exclude_operation'),
    path('some_no_of_data/', some_no_of_data, name='some_no_of_data'),
    path('Q_operation/', Q_operation, name='Q_operation'),
]
