from django.db import models
from datetime import datetime
# Create your models here.
# For changes send with migrations 
# python manage.py makemigrations

# Blog General Settings
class Blogs(models.Model): 
    page_title = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)
    comment_auto_approve = models.BooleanField(default=False)
    
# Blog post models
class post(models.Model):
    title = models.CharField(max_length=255)
    is_allow_comments = models.BooleanField(default=False)
    content: models.CharField
    # datetime'ın çalışacağına emin değilim... Kontrol edilmeli.
    created_date = models.DateField(default= datetime.now())

# Comments
class comments(models.Model):
    email = models.CharField(max_length=255)
    fullname = models.CharField(max_length = 255)
    comment = models.CharField(max_length=600)
    created_date = models.DateField(default=datetime.now())



