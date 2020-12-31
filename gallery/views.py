from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.utils import timezone
import datetime
from .models import Gallery
from .forms import NewFormGallery, EditFormGallery


def gallery_list(request):
	gallery = Gallery.objects.all().order_by('-date_posted')
	return render(request, 'gallery/gallery_list.html', {'gallery':gallery})

def gallery_detail(request, slug): 
	gallery_detail = Gallery.objects.get(slug = slug) 
	return render(request, 'gallery/gallery_detail.html', {'gallery_detail':gallery_detail}) 

def gallery_add(request):
	if request.method == "POST":
		form = NewFormGallery(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			image = form.instance
			return redirect('gallery')
	else:
		form = NewFormGallery()
	return render(request, 'home/forms_gallery.html', {'form': form})

def gallery_edit(request, slug):
	gallery = get_object_or_404(Gallery, slug=slug)
	if request.method == "POST":
		form = EditFormGallery(request.POST,request.FILES, instance=gallery)
		if form.is_valid():
			gallery = form.save(commit=False)
			image = form.instance
			gallery.save()
			return redirect('gallery')
	else:
		form = EditFormGallery(instance=gallery)
	return render(request, 'home/forms_gallery.html', {'form': form})

def gallery_delete(request, slug): 
		context ={} 
		gallery = get_object_or_404(Gallery, slug=slug)
		if request.method =="POST": 
				gallery.delete() 
				return redirect('gallery')
		return render(request,'home/delete_confirm.html', context) 
