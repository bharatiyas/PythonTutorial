from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
# View tells Django how to handle a particular URL once it has been received and mapped.
# View maps the incoming request object to a response where response can be:
#   1. HttpResponse
#   2. Rendered response with the help of:
#   			{
#   				context containing model(s),
#   				a template (which displays the values in that model)
#   			}


# To create a view we need to:
# 	1. Create a function which accept an incoming request as a param and returns a HTTP response
#	2. Associate the view with a URL pattern in the urls.py file

def index_view(request):
	return HttpResponse('<h1>Hello World!<h1>')


def products(request):
	return HttpResponse('Products')

def books(request):
	books = Book.objects.all()
	# return HttpResponse(books)

	# Create a context and pass to the template
	books_context = {
		'book_list': books
	}
	return render(request, 'myapp/books.html', context=books_context)  # Book wrapped inside a context

def detail(request, book_id):
	book = Book.objects.get(id=book_id)
	return render(request, 'myapp/detail.html', {'book': book}) 	# Book directly pass the context
