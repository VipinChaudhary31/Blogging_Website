from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
	model = Post
	template_name = 'Home.html'
	ordering = ['-post_date']

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-', ' '))
	return render(request, 'categories.html', {'cats':cats.title()replace('-', ' '), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'Article_Details.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'Add_Blog.html'

class AddCategoryView(CreateView):
	model = Category
	# form_class = PostForm
	template_name = 'add_category.html'
	fields = '__all__'

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'Update_Post.html'
	# fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'Delete_Post.html'
	success_url = reverse_lazy('Home')