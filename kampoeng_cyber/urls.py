from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
		path('adminkampoengcyber/', admin.site.urls), #set url to the admin page
		path('', include('home.urls')),
		path('', include('berita.urls')),
		path('', include('gallery.urls')),
		path('imagefit/', include('imagefit.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls' )), #set ckeditor url for uploaded file    
		]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #set media for ckeditor