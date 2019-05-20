from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.db import transaction
from django.contrib import messages
from blogs.forms import postForm
from polls.models import blogpost
import html

# Index
def index(request):
    return render(request, 'index.html',  {'hi': 'Hello Django!'}, content_type='text/html')
# About
def about(request):
    return render(request, 'about.html', content_type='text/html')
# signin
def signin(request):
    #POST
    if(request.method=='POST'):
      user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
      if user is not None:
        login(request, user)
        return redirect('/')
    #GET
    return render(request, 'signin.html', content_type='text/html')
# Sign Out
def signout(request):
    logout(request)
    return redirect('/')

# Blogs Admin 
def posts(request):
    return render(request, 'admin/posts.html',{'posts': blogpost.objects.all()}, content_type='text/html')

        
def post(request):
  #POST
    if(request.method=='POST'):

      details = postForm(request.POST)
      if(details.is_valid()):
        bp = blogpost()
        bp.title = request.POST['title']
        bp.is_allow_comments = True if "is_allow_comments" in request.POST else False
        bp.content = html.escape(request.POST['content'])
        bp.keywords = request.POST['keywords']
        bp.save()
      else:
        return redirect('/post/?error=validations')

      return redirect('/post/')
    #GET
    return render(request, 'admin/post.html', {'date': datetime.now()}, content_type='text/html')  