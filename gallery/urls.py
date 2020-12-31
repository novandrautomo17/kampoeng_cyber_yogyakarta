from django.urls import path
from . import views

urlpatterns = [
    path('galeri-kampoeng/', views.gallery_list, name='gallery'),
    path('galeri-kampoeng/<slug:slug>/', views.gallery_detail, name='gallery-detail'),
    path('tambah-galeri-kampoeng/', views.gallery_add, name='gallery-add'),
    path('edit-galeri-kampoeng/<slug:slug>/', views.gallery_edit, name='gallery-edit'),
    path('hapus-galeri-kampoeng/<slug:slug>/', views.gallery_delete, name='gallery-delete'),
]