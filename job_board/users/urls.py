from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>', views.profile, name='users-profile'),
    path('verifyAccount/<int:id>', views.verifyAccount, name='staff-verify-account'),
    
]   
