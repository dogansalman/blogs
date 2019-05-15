from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Index
def index(request):
    return render(request, 'index.html',  {'hi': 'Hello Django!'}, content_type='text/html')
# About
def about(request):
    return render(request, 'about.html', content_type='text/html')
# Singin
def singin(request):
    #POST
    if(request.method=='POST'):
      user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
      if user is not None:
        login(request, user)
        return redirect('/')
    #GET
    return render(request, 'singin.html', content_type='text/html')
