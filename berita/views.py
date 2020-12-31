from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
import datetime
from .models import News
from .forms import NewFormNews, EditFormNews

def news_list(request):
		news = News.objects.all().order_by('-date_posted')
		paginator = Paginator(news, 9)  # 3 posts in each page
		page = request.GET.get('page')
		try:
				newslist = paginator.page(page)
		except PageNotAnInteger:
						# If page is not an integer deliver the first page
				newslist = paginator.page(1)
		except EmptyPage:
				# If page is out of range deliver last page of results
				newslist = paginator.page(paginator.num_pages)
		return render(request, 'berita/berita_list.html',{'page': page,'newslist': newslist, 'news':news})

def news_detail(request, slug): 
	detail = News.objects.get(slug=slug) 
	return render(request, 'berita/berita_detail.html', {'detail':detail}) 

def add_news(request):
	if request.method == "POST":
		form = NewFormNews(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			image = form.instance
			return redirect('news')
	else:
		form = NewFormNews()
	return render(request, 'home/forms.html', {'form': form})

#eng: edit an item
def news_edit(request, slug):
	news = get_object_or_404(News, slug=slug)
	if request.method == "POST":
		form = EditFormNews(request.POST, request.FILES, instance=news)
		if form.is_valid():
			news.save()
			image = form.instance
			return redirect('news')
	else:
		form = EditFormNews(instance=news)
	return render(request, 'home/forms.html', {'form': form})

# delete view for details 
def news_delete(request, slug): 
		context ={} 
		news = get_object_or_404(News, slug=slug)
		if request.method =="POST": 
				news.delete() 
				return redirect('news')
		return render(request,'home/delete_confirm.html', context) 