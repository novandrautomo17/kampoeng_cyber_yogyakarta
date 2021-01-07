from django.conf import settings
from django.utils import timezone
from django.db import models 
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField #add ckeditor as the field
from django.urls import reverse #slug
# from taggit.managers import TaggableManager

class News(models.Model):
	slug = models.SlugField(null=False, unique=True, verbose_name='URL')
	image = models.ImageField(upload_to='uploads/berita', null=True, blank=False)
	title = models.CharField(max_length=200, blank=False, null=True, verbose_name='Judul')
	article = RichTextUploadingField(blank=True, null=True, verbose_name='Artikel')
	date_posted = models.DateTimeField(auto_now_add=False, auto_now=True)
	# tags = TaggableManager(blank=True, verbose_name='Kategori')

	class Meta:
		verbose_name_plural = "Kegiatan"

	def __str__(self):
		return f"{self.title}, {self.article}"

	def get_absolute_url(self):
			return reverse('news-detail', kwargs={'slug': self.slug}) #get slug url 

	def get_edit_url(self):
			return reverse('news-edit', kwargs={'slug': self.slug}) #get slug url 