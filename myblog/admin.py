from django.contrib import admin
from .models import Post

admin.site.register(Post)   # allow blogpost entry from admin area
