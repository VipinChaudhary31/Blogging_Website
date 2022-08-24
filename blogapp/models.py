from django.db import models

# Create your models here.
# User
class User(models.Model):
	Username=models.CharField(max_length=100, primary_key=True)
	Name=models.CharField(max_length=100)
	Email=models.CharField(max_length=100)
	Password=models.CharField(max_length=100)
	class Meta:
		db_table='User'

# User_Profile
class User_Profile(models.Model):
    Username = models.ForeignKey('User', on_delete=models.CASCADE)
    Bio=models.CharField(max_length=200)
    class Meta:
    	db_table='User_Profile'

# Gaming_Blog
class Gaming_Blog(models.Model):
    Username = models.ForeignKey('User', on_delete=models.CASCADE)
    Blog_Title=models.CharField(max_length=100)
    Published_Date_Time=models.CharField(max_length=100)
    Blog_Content=models.CharField(max_length=500)
    class Meta:
    	db_table='Gaming_Blog'

# Business_Blog
class Business_Blog(models.Model):
    Username = models.ForeignKey('User', on_delete=models.CASCADE)
    Blog_Title=models.CharField(max_length=100)
    Published_Date_Time=models.CharField(max_length=100)
    Blog_Content=models.CharField(max_length=500)
    class Meta:
    	db_table='Business_Blog'

# Programming_Blog
class Programming_Blog(models.Model):
    Username = models.ForeignKey('User', on_delete=models.CASCADE)
    Blog_Title=models.CharField(max_length=100)
    Published_Date_Time=models.CharField(max_length=100)
    Blog_Content=models.CharField(max_length=500)
    class Meta:
    	db_table='Programming_Blog'

# Database_Blog
class Database_Blog(models.Model):
    Username = models.ForeignKey('User', on_delete=models.CASCADE)
    Blog_Title=models.CharField(max_length=100)
    Published_Date_Time=models.CharField(max_length=100)
    Blog_Content=models.CharField(max_length=500)
    class Meta:
    	db_table='Database_Blog'

# Computer_Blog
class Computer_Blog(models.Model):
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    Blog_Title=models.CharField(max_length=100)
    Published_Date_Time=models.CharField(max_length=100)
    Blog_Content=models.CharField(max_length=500)
    class Meta:
    	db_table='Computer_Blog'