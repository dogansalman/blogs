from django.http import HttpResponse
from django.shortcuts import render

# Index
def index(request):
    return render(request, 'index.html',  {'hi': 'Hello Django!'}, content_type='text/html')

# About
def about(request):
    return render(request, 'about.html', content_type='text/html')
      
    