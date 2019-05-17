from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.db import transaction
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
    return render(request, 'admin/posts.html', content_type='text/html')

def post(request):
  #POST
    if(request.method=='POST'):

      p = blogpost()
      p.title = request.POST['title']
      p.created_date = datetime.now()
      p.is_allow_comments = True if "is_allow_comments" in request.POST else False
      p.content = html.escape(request.POST['content'])
      p.save()

      return redirect('/post/')
    #GET
    return render(request, 'admin/post.html', {'date': datetime.now()}, content_type='text/html')  