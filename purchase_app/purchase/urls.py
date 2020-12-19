from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="index"),
    path('bar-chart/', bar_chart, name='bar-chart'),

]