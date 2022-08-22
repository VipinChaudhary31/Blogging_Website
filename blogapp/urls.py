from django.contrib import admin
from django.urls import path
from blogapp.views import*


urlpatterns = [
    path('',Homepage),
    path('Login',Login),
    path('Signup',Signup)
]