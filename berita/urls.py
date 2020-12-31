from django.urls import path
from . import views

urlpatterns = [
    path('kegiatan-kampoeng/', views.news_list, name='news'),
    path('kegiatan-kampoeng/<slug:slug>/', views.news_detail, name='news-detail'),
    path('tambah-kegiatan-kampoeng/', views.add_news, name='news-add'),
    path('edit-kegiatan-kampoeng/<slug:slug>/', views.news_edit, name='news-edit'),
    path('hapus-kegiatan-kampoeng/<slug:slug>/', views.news_delete, name='news-delete'),
]