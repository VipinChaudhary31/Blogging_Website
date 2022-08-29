from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
	model = Post
	template_name = 'Home.html'
	ordering = ['-post_date']

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'Article_Details.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'Add_Blog.html'

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'Update_Post.html'
	# fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'Delete_Post.html'
	success_url = reverse_lazy('Home')