from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length=225)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('Home')


# Create your models here.
class Post(models.Model):
	title= models.CharField(max_length=256)
	title_tag= models.CharField(max_length=256)
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	body=RichTextField(blank=True , null=True)
	#body=models.TextField()
	post_date = models.DateField(auto_now_add=True)
	category = models.CharField(max_length=225, default='coding')

	def __str__(self):
		return self.title + '|' + str(self.author)

	def get_absolute_url(self):
		return reverse('Home')