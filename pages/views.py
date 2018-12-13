from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
	return render(request, "home.html", {})

def about(request):
	from pages.mnames import my_movies
	return render(request, "about.html", {"movies": my_movies})

def contact(request):
	
	if request.method == 'POST':
		form = MovieForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_MOVitem = Movie.objects.all 
			messages.success(request, ('Your Movie Has Been Added To List!'))
			return render(request, "contact.html", {'all_MOVitem': all_MOVitem})

	else:	
		all_MOVitem = Movie.objects.all 
		return render(request, "contact.html", {'all_MOVitem': all_MOVitem})	

def delete(request, list_id):
	item = Movie.objects.get(pk=list_id)	
	item.delete()	
	messages.success(request, ('Movie Has Been Deleted'))
	return redirect('contact')

def seen(request, list_id):
	item = Movie.objects.get(pk=list_id)
	item.watched = True
	item.save()
	return redirect('contact')

def notseen(request, list_id):
	item = Movie.objects.get(pk=list_id)
	item.watched = False
	item.save()
	return redirect('contact')	


def edit(request, list_id):
	if request.method == 'POST':
		MOVitem = Movie.objects.get(pk=list_id)

		form = MovieForm(request.POST or None, instance=MOVitem)

		if form.is_valid():
			form.save()
			messages.success(request, ('Your Movie Has Been Edited!'))
			return redirect('contact')

	else:	
		MOVitem = Movie.objects.get(pk=list_id)
		return render(request, "edit.html", {'MOVitem': MOVitem })	