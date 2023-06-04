from django.db import models
import datetime
import os 

# Create your models here.

class Category(models.Model):   
    name = models.CharField(max_length=150,null=False,blank=False)
