from django.contrib import admin
from .models import Carousel, About, History, Contact

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
	pass

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
	pass

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
	pass

@admin.register(Contact)
class AboutAdmin(admin.ModelAdmin):
  list_display = ("name", "subject")
	