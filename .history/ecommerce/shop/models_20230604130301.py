from django.db import models

# Create your models here.

class Category(models.Model):   
    name = models.CharField(max_length=150,null=False,blank=False)
