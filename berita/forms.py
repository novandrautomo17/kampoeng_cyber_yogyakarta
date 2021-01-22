from django import forms
from django.contrib import admin
from .models import News, Publication
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewFormNews(forms.ModelForm):
		article = forms.CharField(widget=CKEditorUploadingWidget())
		class Meta:
				model = News
				fields = ('slug', 'image', 'title', 'article')
				widgets = {
					'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'URL', 'id':"name"}),
					'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Judul', 'id':"subject"}),
					'article': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Konten', 'rows':'20'}),
				}


class EditFormNews(forms.ModelForm):
		article = forms.CharField(widget=CKEditorUploadingWidget())
		class Meta:
				model = News
				fields = ('slug', 'image', 'title', 'article')
				widgets = {
					'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'URL', 'id':"name"}),
					'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Judul', 'id':"subject"}),
					'article': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Konten', 'rows':'20'}),
				}

class NewFormPublication(forms.ModelForm):
		article = forms.CharField(widget=CKEditorUploadingWidget())
		class Meta:
				model = Publication
				fields = ('slug', 'image', 'title', 'article')
				widgets = {
					'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'URL', 'id':"name"}),
					'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Judul', 'id':"subject"}),
					'article': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Konten', 'rows':'20'}),
				}


class EditFormPublication(forms.ModelForm):
		article = forms.CharField(widget=CKEditorUploadingWidget())
		class Meta:
				model = Publication
				fields = ('slug', 'image', 'title', 'article')
				widgets = {
					'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'URL', 'id':"name"}),
					'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Judul', 'id':"subject"}),
					'article': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Konten', 'rows':'20'}),
				}