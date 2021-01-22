import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Carousel, About, History
from berita.models import News
from gallery.models import Gallery
from .forms import ContactForm, CarouselForm, AboutForm, HistoryForm
from django.contrib import messages
from django.core.mail import EmailMessage, BadHeaderError #check email badheader on the contactform

def landingpage(request):
	carousel = Carousel.objects.all()
	about = About.objects.all()
	news = News.objects.all().order_by('-date_posted')[0:3]
	gallery = Gallery.objects.all().order_by('-date_posted')[0:3]

#contactform on landingpage
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			''' Begin reCAPTCHA validation '''
			recaptcha_response = request.POST.get('g-recaptcha-response')
			data = {
			    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			    'response': recaptcha_response
			}
			r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
			result = r.json()
			''' End reCAPTCHA validation '''			
			post = form.save()
			post.save()
			subject = post.subject
			email = post.email
			message = f"Nama: {post.name} \n \nPesan: {post.message}"
			messages.success(request, 'Pesan anda telah kami terina, terima kasih telah menghubungi kami.')
			try:
				mail=EmailMessage(
					subject = subject,
					body=message,
					from_email='warga@kampoengcyber.id', 
					to=['warga@kampoengcyber.id'],	
					headers={'Reply-To': email})#where you want replies to go
				mail.send()
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('landingpage')
	return render(request, 'home/landingpage.html', {'carousel':carousel, 'about':about, 'news':news, 'gallery':gallery ,'form': form})


def edit_landingpage(request):
	return render(request, 'home/edit_landingpage.html')

#eng: edit an item
def edit_carousel(request, pk):
	carousel = get_object_or_404(Carousel, pk=pk)
	if request.method == "POST":
		form = CarouselForm(request.POST, request.FILES, instance=carousel)
		if form.is_valid():
			carousel.save()
			image = form.instance
			return redirect('landingpage')
	else:
		form = CarouselForm(instance=carousel)
	return render(request, 'home/forms_edit_carousel.html', {'form': form})

def profile(request):
	about = About.objects.all()
	return render(request, 'home/profile.html', {'about':about})

def edit_about(request, pk):
	about = get_object_or_404(About, pk=pk)
	if request.method == "POST":
		form = AboutForm(request.POST, request.FILES, instance=about)
		if form.is_valid():
			about.save()
			image = form.instance
			return redirect('profile')
	else:
		form = AboutForm(instance=about)
	return render(request, 'home/forms_edit_about.html', {'form': form})

def history(request):
	history = History.objects.all()
	return render(request, 'home/history.html', {'history':history})

def edit_history(request, pk):
	history = get_object_or_404(History, pk=pk)
	if request.method == "POST":
		form = HistoryForm(request.POST, request.FILES, instance=history)
		if form.is_valid():
			history.save()
			image = form.instance
			return redirect('history')
	else:
		form = HistoryForm(instance=history)
	return render(request, 'home/forms_edit_history.html', {'form': form})
