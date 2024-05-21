from django.db import models

# Create your models here. Django will automatically create tables based on the models defined here.
# We define models in terms of classes

class Book(models.Model):
	name = models.CharField(max_length=100)
	desc = models.CharField(max_length=300)
	price = models.IntegerField()

	# This is same as toString() in Java
	def __str__(self):
		return f"name: {self.name}, desc: {self.desc}, price: {self.price}"

# Making Migrations - Process of creating tables out of models
# Commands to make migration (stop the server if already running)
# The following command will look at models.py and determine if any new models have been created
# $ python3 manage.py makemigrations

# But the tables are not created as a part of the previous step. To create the tables
# $ py manage.py migrate

# Start Python shell
# $ py manage.py shell

# Import the models into the shell
# >>> from myapp.models import Book

# Check if this model has any object/any data. This should return <QuerySet []> because there is no data present
# >>> Book.objects.all()

# To save some data into that table then we need to create Book object and then store it
# >>> a = Book(name="Life of a Pi", desc="Book on a journey of a boy named Pi", price=10)

# Save the object created above
# >>> a.save()

# Now if you retrieve records from the Book table you will get <QuerySet [<Book: Book object (1)>]>
# >>> Book.objects.all()

# To retrieve the book object we need a string representation in the class

# Create Super user for the DB
# $ py manage.py createsuperuser

