from django.urls import path
from . import views


urlpatterns = [
     path('registration/', views.registration , name='registration'),
     path ('registerpage/', views.mypage , name='myregisterpage'),
     path ('home/', views.home , name='myhome'),
     path ('login/', views.login , name='mylogin'),
     path ('contact/', views.contact , name='mycontact'),
     path ('about/', views.about , name='myabout'),
     path ('dashboard/', views.dashboard , name='mydashboard')
]




