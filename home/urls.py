from django.urls import path
from . import views

#this url patterns is looking to views.py in blog app directory
urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('edit-landingpage/', views.edit_landingpage, name='edit-landingpage'),
    path('edit-carousel-kampoeng-cyber-yogyakarta/<int:pk>/', views.edit_carousel, name='carousel-edit'),
    path('edit-profile-kampoeng-cyber-yogyakarta/<int:pk>/', views.edit_about, name='about-edit'),
    path('edit-history-kampoeng-cyber-yogyakarta/<int:pk>/', views.edit_history, name='history-edit'),
    path('profil-kampoeng-cyber/', views.profile, name='profile'),
    path('sejarah-kampoeng-cyber/', views.history, name='history'),
]