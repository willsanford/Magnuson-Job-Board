from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='staff-home'),
    path('addCompany/', views.addCompany, name='staff-add-company'),
    path('addJob/', views.addJob, name='staff-add-job'),
]   
