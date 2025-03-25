
from datetime import date, datetime
# from django.utils.timezone import now
from email.policy import default
from urllib import request
from xmlrpc.client import DateTime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from accounts.models import Jobseeker

class Jobtype(models.Model):
    type_title=models.CharField(max_length=255)
    def __str__(self):
        return self.type_title
   
class Experience(models.Model):
    e_title=models.CharField(max_length=255)
    def __str__(self):
        return self.e_title
   
class Category(models.Model):
    title=models.CharField(max_length=255)
    def __str__(self):
        return self.title
    
class Joblist(models.Model):
    j_title=models.CharField(max_length=255)
    company=models.CharField(max_length=255)
    type=models.ForeignKey(Jobtype,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    location=models.CharField(max_length=255)
    min_salary=models.CharField(max_length=100)
    max_salary=models.CharField(max_length=100)
    skills=models.CharField(max_length=255)
    education=models.CharField(max_length=255)
    exp=models.ForeignKey(Experience,on_delete=models.CASCADE)
    job_desc=models.TextField()
    no_of_vacancy=models.IntegerField()
    date_created=models.DateTimeField(default=timezone.now)
    last_date=models.DateField()
    logo=models.ImageField(upload_to='pics')
    c_website=models.URLField()
    c_overview=models.TextField()
    mobile=models.CharField(max_length=10)
    email=models.EmailField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.j_title
    def is_end_date(self):
        if date.today() > self.last_date:
            return True
            
        else:
            pass
 
    
class AppliedList(models.Model):
    candidate=models.ForeignKey(Jobseeker,on_delete=models.CASCADE)
    job=models.ForeignKey(Joblist,on_delete=models.CASCADE)
    resume=models.FileField(upload_to='cv')
    status=models.CharField(max_length=20,default=0)
    apply_date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.job.j_title