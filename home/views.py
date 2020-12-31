from django.shortcuts import render, redirect 
from django.conf import settings
from .models import Carousel, About
from berita.models import News
from gallery.models import Gallery
from .forms import ContactForm
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
			post = form.save()
			post.save()
			subject = post.subject
			email = post.email
			message = f"Nama: {post.name} \n \nPesan: {post.message}"
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