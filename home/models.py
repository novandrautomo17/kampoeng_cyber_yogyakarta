from django.conf import settings
from django.utils import timezone
from django.db import models 
from django.urls import reverse #slug
from PIL import Image

class Carousel(models.Model):        
	image1 = models.ImageField(upload_to='carousel', blank=False, null=True)
	caption_image_1 = models.CharField(max_length=200, blank=False, null=True)
	image2 = models.ImageField(upload_to='carousel', blank=False, null=True)
	caption_image_2 = models.CharField(max_length=200, blank=False, null=True)
	image3 = models.ImageField(upload_to='carousel', blank=False, null=True)
	caption_image_3 = models.CharField(max_length=200, blank=False, null=True)
	image4 = models.ImageField(upload_to='carousel', blank=False, null=True)
	caption_image_4 = models.CharField(max_length=200, blank=False, null=True)

	class Meta:
		verbose_name_plural = "Carousel"

	def __str__(self):
		return f"Carousel" 

class About(models.Model):        
	title_about = models.CharField(max_length=200, blank=False, null=True)
	about_desc = models.TextField(blank=False, null=True)
	about_image = models.ImageField(upload_to='about_image', blank=False, null=True)

	class Meta:
		verbose_name_plural = "About"

	def __str__(self):
		return f"About" 

class Contact(models.Model):        
	name = models.CharField(max_length=500, blank=False, null=True, verbose_name='Nama')
	email = models.CharField(max_length=200, blank=False, null=True, verbose_name='Alamat e-mail')
	subject = models.CharField(max_length=500, blank=False, null=True, verbose_name='Subject')
	message = models.TextField(blank=False, null=True, verbose_name='Message')

	class Meta:
		verbose_name_plural = "Contact"

	def __str__(self):
		return f"{self.subject} {self.name}" 
