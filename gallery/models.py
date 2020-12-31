from django.conf import settings
from django.utils import timezone
from django.db import models 
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

class Gallery(models.Model):
	slug = models.SlugField(null=False, unique=True, verbose_name='URL')
	title = models.CharField(max_length=200, blank=False, null=True, verbose_name='Judul')
	image = models.ImageField(upload_to='uploads/gallery', null=True, blank=True)
	caption = models.TextField(blank=False, null=True)
	date_posted = models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		verbose_name_plural = "Galeri"

	def __str__(self):
		return f"{self.caption}, {self.date_posted}"

	def get_absolute_url(self):
			return reverse('gallery-detail', kwargs={'slug': self.slug}) #get slug url 
