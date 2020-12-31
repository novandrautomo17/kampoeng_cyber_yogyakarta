from django import forms
from .models import Contact, Carousel, About


class CarouselForm(forms.ModelForm):
	class Meta:
		model = Carousel
		fields = ('image1', 'caption_image_1', 'image2', 'caption_image_2', 'image3', 'caption_image_3', 'image4', 'caption_image_4')

class AboutForm(forms.ModelForm):
	class Meta:
		model = About
		fields = ('title_about', 'about_desc', 'about_image')

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

