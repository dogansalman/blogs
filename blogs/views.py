from django.http import HttpResponse
from django.shortcuts import render

# Pages setting
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# About Templates
def about(request):
 return render(request, 'about.html', {  'hi': 'Hello Django',}, content_type='text/html')
      
    