from django.contrib import admin
from .models import News, Publication

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "date_posted")

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "date_posted")
