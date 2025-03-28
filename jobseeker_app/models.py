from django.db import models

from accounts.models import Jobseeker
class Resume(models.Model):
    owner=models.ForeignKey(Jobseeker,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=15,default=0)
    ptitle=models.CharField(max_length=255)
    linkedlin=models.URLField()
    objective=models.TextField()
    dob=models.DateField()
    gender=models.CharField(max_length=15)
    education_institute=models.CharField(max_length=255)
    ecourse=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    start=models.CharField(max_length=255)
    end=models.CharField(max_length=255)
    masters_name=models.CharField(max_length=255,default=0)
    m_college=models.CharField(max_length=255,default=0)
    m_location=models.CharField(max_length=255,default=0)
    m_start=models.CharField(max_length=255,default=0)
    m_end=models.CharField(max_length=255,default=0)
   
    exp_title=models.CharField(max_length=255)
    exp_company=models.CharField(max_length=255)
    exp_place=models.CharField(max_length=255)
    start_year=models.CharField(max_length=255)
    end_year=models.CharField(max_length=255)
    exp_title2=models.CharField(max_length=255,default=0)
    exp_company2=models.CharField(max_length=255,default=0)
    exp_place2=models.CharField(max_length=255,default=0)
    start_year2=models.CharField(max_length=255,default=0)
    end_year2=models.CharField(max_length=255,default=0)
    skills=models.CharField(max_length=255)
    pro_pic=models.ImageField(upload_to='pics')
    create_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name
