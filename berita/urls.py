from django.urls import path
from . import views

urlpatterns = [
    path('berita-kampoeng-cyber-yogyakarta/', views.news_list, name='news'),
    path('berita-kampoeng-cyber-yogyakarta/<slug:slug>/', views.news_detail, name='news-detail'),
    path('tambah-berita-kampoeng-cyber-yogyakarta/', views.add_news, name='news-add'),
    path('edit-berita-kampoeng-cyber-yogyakarta/<slug:slug>/', views.news_edit, name='news-edit'),
    path('hapus-berita-kampoeng-cyber-yogyakarta/<slug:slug>/', views.news_delete, name='news-delete'),

    path('publikasi-kampoeng-cyber-yogyakarta/', views.publication_list, name='publication'),
    path('publikasi-kampoeng-cyber-yogyakarta/<slug:slug>/', views.publication_detail, name='publication-detail'),
    path('tambah-publikasi-kampoeng-cyber-yogyakarta/', views.add_publication, name='publication-add'),
    path('edit-publikasi-kampoeng-cyber-yogyakarta/<slug:slug>/', views.publication_edit, name='publication-edit'),
    path('hapus-publikasi-kampoeng-cyber-yogyakarta/<slug:slug>/', views.publication_delete, name='publication-delete'),
]