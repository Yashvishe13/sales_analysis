from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.data_entry, name='data_entry'),
]