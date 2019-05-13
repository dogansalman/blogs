from django.db import models
from datetime import datetime
# Create your models here.
# For changes send with migrations 
# python manage.py makemigrations

# Blog General Settings
class Blogs(models.Model): 
    page_title = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)
    
# Blog post models
class post(models.Model):
    title = models.CharField(max_length=255)
    is_allow_comments = models.BooleanField(default=False)
    content: models.CharField
    # datetime'ın çalışacağına emin değilim... Kontrol edilmeli.
    created_date = models.DateField(default= datetime.now())



