from django import forms
from .models import Contact, Carousel, About, History
from ckeditor_uploader.widgets import CKEditorUploadingWidget



class CarouselForm(forms.ModelForm):
	class Meta:
		model = Carousel
		fields = ('image1', 'caption_image_1', 'image2', 'caption_image_2', 'image3', 'caption_image_3', 'image4', 'caption_image_4')
		widgets = {
		  'caption_image_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Caption Foto 1', 'id':"Caption"}),
		  'caption_image_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Caption Foto 2', 'id':"Caption"}),
		  'caption_image_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Caption Foto 3', 'id':"Caption"}),
		  'caption_image_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Caption Foto 4', 'id':"Caption"}),
		}

class AboutForm(forms.ModelForm):
	class Meta:
		model = About
		fields = ('title_about', 'about_desc', 'about_image')
		widgets = {
		  'title_about': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title', 'id':"Title"}),
		  'about_desc': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Deskripsi', 'id':"Deskripsi"}),
		}

class HistoryForm(forms.ModelForm):
	article = forms.CharField(widget=CKEditorUploadingWidget())	
	class Meta:
		model = History
		fields = ('article',)
		widgets = {
			'article': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Deskripsi', 'rows':'20'}),
		}

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('name', 'email', 'subject', 'message')
		widgets = {
		  'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nama', 'id':"name"}),
		  'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Alamat e-mail', 'id':"email"}),
		  'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Subject', 'id':"subject"}),
		  'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Pesan', 'rows':'9'}),
		}