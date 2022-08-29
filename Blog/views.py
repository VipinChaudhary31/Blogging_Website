from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
# def Home(request):
# 	return render(request, 'Home.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'Home.html'

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'Article_details.html'