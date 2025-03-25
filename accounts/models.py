
from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255,null=True)
    company=models.CharField(max_length=255,null=True)
    designation=models.CharField(max_length=255,null=True)
    mobile=models.CharField(max_length=12,null=True)
    type=models.CharField(max_length=15,null=True)
    status=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=255,default=0)
    district=models.CharField(max_length=255,default=0)
    pin=models.CharField(max_length=25,default=0)
    city=models.CharField(max_length=255,default=0)
    state=models.CharField(max_length=255,default=0)
    country=models.CharField(max_length=255,default=0)
    url=models.URLField(default=0)
    image=models.ImageField(upload_to='pics',default=0)
    comp_desc=models.TextField(default=0)
    found_year= models.CharField(max_length=30,default=0)

    no_of_employees=models.CharField(max_length=255,default=0)
    register_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
class Jobseeker(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=12,null=True)
    type=models.CharField(max_length=15,null=True)
    status=models.CharField(max_length=20,null=True)
    register_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.email
    
    


