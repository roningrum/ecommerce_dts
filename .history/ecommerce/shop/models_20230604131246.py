from django.db import models
import datetime
import os 

# Create your models here.

def getFileName(request, filename): 
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time, filename)
    return os.path.join('uploads/',new_filename)

class Category(models.Model):   
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=False)
    description=models.TextField(max_length=500, null=False, blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)