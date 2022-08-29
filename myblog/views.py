from django.shortcuts import render
from django.views.generic import ListView, DetailView # listview use to give all data from database and detailview give specific data
from .models import Post
#def home(request):
#	return render(request,'home.html',{})

#we use class instead of def when use listview adn detailview
class HomeView(ListView):
	model=Post
	template_name = 'home.html'	

class ArticleDetailView(DetailView):
	model=Post
	template_name='article_details.html'