from django.db import models

# Create your models here.

class Text(models.Model):
    title = models.TextField(null=True,blank=True)
    author = models.PositiveIntegerField(null=True,blank=True)
    translator = models.PositiveIntegerField(null=True,blank=True)
    entry = models.PositiveIntegerField(null=True,blank=True)
    link = models.TextField(null=True,blank=True)
    text = models.TextField(null=True,blank=True)
    date = models.DateField(auto_now=False,auto_now_add=True,null=True,blank=False)