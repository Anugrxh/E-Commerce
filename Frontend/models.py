from django.db import models

# Create your models here.

class contactdb(models.Model):
    fullname = models.CharField(max_length=50,blank=True,null=True)
    contactnumber = models.IntegerField(blank=True,null=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    suggestion = models.CharField(max_length=50,null=True,blank=True)

class signupdb(models.Model):
    fullname = models.CharField(max_length=50,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    username = models.CharField(max_length=50,null=True,blank=True)
    password = models.CharField(max_length=50,null=True,blank=True)

class cartdb(models.Model):
    username = models.CharField(max_length=50,null=True,blank=True)
    pname = models.CharField(max_length=50,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    totalprice = models.IntegerField(null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)

class bookingdb(models.Model):
    username=models.CharField(max_length=20,null=True,blank=True)
    fullname=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=20,null=True,blank=True)
    address=models.CharField(max_length=80,null=True,blank=True)
    city=models.CharField(max_length=80,null=True,blank=True)
    bookedproduct=models.CharField(max_length=80,null=True,blank=True)
    pincode=models.IntegerField(null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    totalprice=models.IntegerField(null=True,blank=True)