from django.db import models
from datetime import datetime
# Create your models here.
# For changes send with migrations 
# python manage.py makemigrations

# Blog General Settings
class blogs(models.Model): 
    page_title = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)
    comment_auto_approve = models.BooleanField(default=False)
    
# Blog post models
class blogpost(models.Model):
    title = models.CharField(max_length=255)
    is_allow_comments = models.BooleanField(default=False)
    content = models.TextField
    created_date = models.DateField

# Comments
class comments(models.Model):
    email = models.CharField(max_length=255)
    fullname = models.CharField(max_length = 255)
    comment = models.CharField(max_length=600)
    created_date = models.DateField
