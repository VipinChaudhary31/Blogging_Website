from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from email import message
import email
import smtplib

def Mailblog(request):
	model = Post.objects.all()
	SERVER = "SMTP-mail.outlook.com"
	FROM = "lucifergod648@hotmail.com"
	TO = ["vipinchaudhary31122002@hotmail.com"] # must be a list
	SUBJECT = model[0]
	TEXT = "hello vipin its is nice ot meet you!"
	# Prepare actual message
	message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

	%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

	# Send the mail
	import smtplib
	server = smtplib.SMTP(SERVER)
	server.starttls()
	server.login("lucifergod648@hotmail.com", "KINGOFHELL$")
	server.sendmail(FROM, TO, message)
	server.quit()
	return HttpResponse("message send!")

class HomeView(ListView):
	model = Post
	template_name = 'Home.html'
	ordering = ['-post_date']

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-', ' '))
	return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})

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