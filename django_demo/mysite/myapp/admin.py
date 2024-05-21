from django.contrib import admin
from .models import Book

# Register your models here.

# You need to register your model for Django to include it inside your DB admin panel. And then you can perform CRUD
# operations in the table

admin.site.register(Book)		# In the admin panel it will appear as Books


