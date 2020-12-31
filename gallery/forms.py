from django import forms
from .models import Gallery

class NewFormGallery(forms.ModelForm):
		class Meta:
				model = Gallery
				fields = ('slug', 'title', 'image', 'caption')
				widgets = {
					'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'URL', 'id':"name"}),
					'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Judul', 'id':"subject"}),
					'caption': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Caption', 'rows':'9'}),
				}

class EditFormGallery(forms.ModelForm):
		class Meta:
				model = Gallery
				fields = ('slug', 'title', 'image', 'caption')
				widgets = {
					'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'URL', 'id':"name"}),
					'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Judul', 'id':"subject"}),
					'caption': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Caption', 'rows':'9'}),
				}