from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='company-home'),
    path('signup/', views.signUp, name='company-sign-up'),
    path('add/', views.add, name='company-add'),
]   
