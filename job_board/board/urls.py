from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='board-home'),
    path('about/', views.about, name='board-about'),
    path('search/', views.search, name='board-search'),
    path('job/<int:id>', views.single_job, name='board-single-job'),
    path('company/<int:id>', views.single_company, name='board-single-company')
]   
