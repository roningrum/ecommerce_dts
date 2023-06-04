from django.db import models
import datetime
import os 

# Create your models here.

def getFileName(request, filename): 
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")

class Category(models.Model):   
    name = models.CharField(max_length=150,null=False,blank=False)
