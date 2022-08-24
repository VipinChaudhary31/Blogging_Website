from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt       # to fetch data from user input fields
# from blogapp.models import *    # for database import



def Homepage(request):
	return render(request,'Homepage.html')

def Login(request):
	return render(request,'Login.html')

def Signup(request):
	return render(request,'Login.html')

# def Signup_User(request):
# 	    if request.method=="POST":   
#             username = request.POST['Username']
#             email = request.POST['Email']
#             name = request.POST['Name']
#             password1 = request.POST['Password']
#             user = User(Username, Email, Name, Password)
#             user.save()
#             return render(request, 'Login.html')   
#     return render(request, "Signup.html")



	
	

