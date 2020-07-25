from django.db import models
from django.urls import reverse


class Memories(models.Model):
    title=models.CharField(max_length=100,default=None,null=True,verbose_name="Title")
    image=models.FileField(upload_to="images/")

    def __str__(self):
        return self.title
    
    

class Jayanth(models.Model):
    email=models.CharField(max_length=50,primary_key=True,default=None,verbose_name="Email")
    password=models.CharField(max_length=50,default=None,verbose_name="Password")

class Stories(models.Model):
    title=models.CharField(max_length=100,default=None,null=True,verbose_name="Title")
    Story=models.CharField(max_length=10000,default=None,null=True,verbose_name="Content")

    def __str__(self):
        return self.title


class Videos(models.Model):
    title=models.CharField(max_length=100,default=None,null=True,verbose_name="Title")
    video=models.FileField(upload_to="videos/")
    
    def __str__(self):
        return self.title

    
    
    
    

