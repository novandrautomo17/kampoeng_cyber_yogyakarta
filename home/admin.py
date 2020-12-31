from django.contrib import admin
from .models import Carousel, About, Contact

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
	pass

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
	pass

@admin.register(Contact)
class AboutAdmin(admin.ModelAdmin):
  list_display = ("name", "subject")
	