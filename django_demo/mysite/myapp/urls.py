"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views


# Assigning a name for the app so that you can use namespaces for the URL mapping. This is helpful when you have
# multiple apps and you want to use namespaces for the URLs. These namespacing is then used inside the template HTML
app_name = 'myapp'

urlpatterns = [
    path('books/', views.books, name='books'),
    path('books/<int:book_id>/', views.detail, name='detail_url'),  # Tha name is used to reference the URL in html template files

]
