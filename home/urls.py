from django.urls import path
from . import views

#this url patterns is looking to views.py in blog app directory
urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('profil-kampoeng-cyber/', views.profile, name='profile'),
    path('sejarah-kampoeng-cyber/', views.history, name='history'), 

]