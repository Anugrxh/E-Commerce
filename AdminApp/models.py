from django.db import models

# Create your models here.


class catagorydb(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=200 , null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)

class productdb(models.Model):
    catname = models.CharField(max_length=50,null=True,blank=True)
    productname = models.CharField(max_length=50,null=True,blank=True)
    description = models.CharField(max_length=150,null=True,blank=True)
    price = models.CharField(max_length=20,null=True,blank=True)
    image = models.ImageField(upload_to="profile",null=True,blank=True)
