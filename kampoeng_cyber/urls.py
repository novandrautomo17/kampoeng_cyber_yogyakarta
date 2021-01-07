from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
		path('adminkampoengcyber/', admin.site.urls), #set url to the admin page
		path('loginkampoengcyber/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
		path('logoutkampoengcyber/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
		path('', include('home.urls')),
		path('', include('berita.urls')),
		path('', include('gallery.urls')),
		path('imagefit/', include('imagefit.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls' )), #set ckeditor url for uploaded file    
		]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #set media for ckeditor