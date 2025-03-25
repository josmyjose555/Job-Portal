from datetime import date
from datetime import datetime
import email
import imp
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render,redirect
from employer_app.models import Joblist,Category,Experience,AppliedList
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from accounts.models import Employer,Jobseeker 
from jobseeker_app.models import Resume 
from django.contrib.auth.models import User
# pdf===================
# importing the necessary libraries
# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View
from .models import Resume
from .process import html_to_pdf 
from django.template.loader import render_to_string

#Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        user=request.user.id
        profile=Jobseeker.objects.get(user=user)
        data =Resume.objects.filter(owner=profile).last()
        open('templates/temp.html', "w",encoding="utf-8").write(render_to_string('resume_page.html', {'resume': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
  








#  ---------------------------------------------------------------------------------------------------


# Create your views here.
def jobseeker_joblist(request):
    user=request.user


    jobseeker=Jobseeker.objects.get(user=user)
    data=AppliedList.objects.filter(candidate=jobseeker)
    li=[]
    for i in data:
        li.append(i.job.id)
    e=Experience.objects.all()
    jobm=Joblist.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(jobm, 6)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages) 
    
    
    return render(request,'jobseeker_joblist.html',{'jobm':post,'e':e,'li':li})

    ################################################################

def jobseeker_profile(request):
    user=request.user.id
    profile=Jobseeker.objects.get(user=user)
    res=Resume.objects.filter(owner=profile).last()
    return render(request,'jobseeker_profile.html',{'res':res})

def edit_jobseeker_profile(request,jid):

    
    res=Resume.objects.get(owner=jid)
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        mail=request.POST['email']
        phone=request.POST['phone']
        title =request.POST['title']
        linkedlin=request.POST['link']
        objective=request.POST['objective']
        gender =request.POST['gender']
        dob =request.POST['dob']
        master=request.POST['master']
        m_college=request.POST['collegem']
        m_place=request.POST['statem']
        m_start=request.POST['startm']
        m_end=request.POST['endm']
        college_name=request.POST['college']
        degree= request.POST['degree']
        start_year =request.POST['start']
        end_year =request.POST['end']
        place =request.POST['state']
        exp_company=request.POST['company']
        exp_position=request.POST['position'] 
        exp_place =request.POST['location']
        exp_start=request.POST['syear'] 
        exp_end =request.POST['eyear']
        exp_company2=request.POST['company2']
        exp_position2=request.POST['position2'] 
        exp_place2 =request.POST['location2']
        exp_start2=request.POST['syear2'] 
        exp_end2=request.POST['eyear2']
        skills =request.POST['skills']
        res.first_name=first_name
        res.last_name=last_name
        res.phone=phone
        res.email=mail
        res.ptitle=title
        res.linkedlin=linkedlin
        res.objective=objective
        res.dob=dob
        res.gender=gender
        res.education_institute=college_name
        res.ecourse=degree
        res.location=place
        res.start=start_year
        res.end=end_year
        res.masters_name=master
        res.m_college=m_college
        res.m_location=m_place
        res.m_start=m_start
        res.m_end=m_end
        res.exp_title=exp_position
        res.exp_company=exp_company
        res.exp_place=exp_place
        res.start_year=exp_start
        res.end_year=end_year
        res.exp_title2=exp_position2
        res.exp_company2=exp_company2
        res.exp_place2=exp_place2
        res.start_year2=exp_start2
        res.end_year2=exp_end2
        res.skills=skills
        res.save()

    return render(request,'edit_jobseeker_profile.html',{'res':res})






    #######################################################################################
def j_jobdetails(request,myid):

    joblist1=Joblist.objects.filter(pk=myid)
    user=request.user


    jobseeker=Jobseeker.objects.get(user=user)
    data=AppliedList.objects.filter(candidate=jobseeker)
    li=[]
    for i in data:
        li.append(i.job.id)
    return render(request,'j_jobdetails.html',{'joblist':joblist1,'li':li})

def jobseeker_saved_jobs(request):
    return render(request,'jobseeker_saved_jobs.html')
def jobseeker_change_pass(request):
    error=""
    if request.method=='POST':
        c=request.POST['current_password']
        n=request.POST['user_new_password']
        if len(n)<8 or len(n)<20:
            messages.info(request,"password must contain 8 characters")
            return redirect('/jobseeker/jobseeker_change_pass/')
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d={"error":error}    
    return render(request,'jobseeker_change_pass.html',d)

def jobseeker_create_cv(request):
    user=request.user.id
    j=Jobseeker.objects.filter(user=user)
    resume=Resume.objects.filter(owner=j)
    
        
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        mail=request.POST['email']
        phone=request.POST['phone']
        title =request.POST['title']
        linkedlin=request.POST['link']
        objective=request.POST['objective']
        gender =request.POST['gender']
        dob =request.POST['dob']
        master=request.POST['master']
        m_college=request.POST['collegem']
        m_place=request.POST['statem']
        m_start=request.POST['startm']
        m_end=request.POST['endm']
        college_name=request.POST['college']
        degree= request.POST['degree']
        start_year =request.POST['start']
        end_year =request.POST['end']
        place =request.POST['state']
        exp_company=request.POST['company']
        exp_position=request.POST['position'] 
        exp_place =request.POST['location']
        exp_start=request.POST['syear'] 
        exp_end =request.POST['eyear']
        exp_company2=request.POST['company2']
        exp_position2=request.POST['position2'] 
        exp_place2 =request.POST['location2']
        exp_start2=request.POST['syear2'] 
        exp_end2=request.POST['eyear2']
        skills =request.POST['skills']

        


        pro_pic=request.FILES['pro']
        user=request.user
        job=Jobseeker.objects.get(user=user)
        resume_ob=Resume.objects.create(owner=job,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        email=mail,
        ptitle=title,
        linkedlin=linkedlin,objective=objective,dob=dob,
        gender=gender,education_institute=college_name,ecourse=degree,location=place,start=start_year,
        end=end_year,masters_name=master,m_college=m_college,m_location=m_place,m_start=m_start,m_end=m_end,exp_title=exp_position,exp_company=exp_company,exp_place=exp_place,
        start_year=exp_start,end_year=exp_end,exp_title2=exp_position2,exp_company2=exp_company2,exp_place2=exp_place2,
        start_year2=exp_start2,end_year2=exp_end2,
        
        skills=skills,pro_pic=pro_pic,create_date=datetime.now())
        resume_ob.save();
        return redirect('/jobseeker/resume_page/')
   
    return render(request,'jobseeker_create_cv.html',{'resume':resume})


def resume_page(request):
    user=request.user
    job=Jobseeker.objects.get(user=user)
    # res=Resume.objects.get(owner=job)
    res=Resume.objects.filter(owner=job).last()
    return render(request,'resume_page.html',{'resume':res})  

def jobseeker_applied_job(request):
    user=request.user
    jobseeker=Jobseeker.objects.get(user=user)
    myjobs=AppliedList.objects.filter(candidate=jobseeker)
    return render(request,'jobseeker_applied_job.html',{'myjobs':myjobs})
def apply_job(request,pid):
    user=request.user.id
    applicant=Jobseeker.objects.get(user_id=user)
    job=Joblist.objects.get(id=pid)
    
   
    if request.method=='POST':
        resume = request.FILES['resume']
        AppliedList.objects.create(job=job,candidate=applicant,resume=resume,status='Applied',apply_date=date.today())
        
        return redirect('/jobseeker/jobseeker_applied_job')

    return render(request,'apply_job.html',{'job':job})
##############################################################################################

def jobseeker_search(request):
    user=request.user


    jobseeker=Jobseeker.objects.get(user=user)
    data=AppliedList.objects.filter(candidate=jobseeker)
    li=[]
    for i in data:
        li.append(i.job.id)





    job=Joblist.objects.all()
    categories=Category.objects.all()
    e=Experience.objects.all()
    location=request.GET.get('location')
    categorys=request.GET.get('categorys')
    exp=request.GET.get('exp')
    k=request.GET.get('k')
    if location !=''  and  location is not None and k !='' and k is not None and exp !='' and exp is not None :   #(3 condition must satisfy (skill +location + experience))
        job=job.filter(Q(location__icontains=location) 
        & (Q(skills__icontains=k) | Q(j_title__icontains=k))
        & Q(exp__e_title__icontains=exp)).distinct()

    elif location !=''  and  location is not None and k !='' and k is not None :   # (2 condition must location+ skill)
        job=job.filter(Q(location__icontains=location) 
        & (Q(skills__icontains=k)| Q(j_title__icontains=k) )).distinct()
        
    elif k!='' and k is not None and exp !='' and exp is not None:          # (2 condition must true  experience + skill)
        job=job.filter(Q(skills__icontains=k) | Q(j_title__icontains=k)
        & Q(exp__e_title__icontains=exp)).distinct() 
    
    elif location !='' and location is not None:      # (only location )
        job=job.filter(location__icontains=location)
    
    elif categorys !='' and categorys is not None:    #(only category)
        job=job.filter(category__title=categorys)
    elif k !='' and k is not None:                # (search based on skills or company name or title )
        job=job.filter(Q(j_title__icontains=k) | Q(skills__icontains=k) |Q(company__icontains=k)).distinct()
    
    elif exp !='' and exp is not None:
        job=job.filter(exp__e_title__icontains=exp)
   
    return render(request,'jobseeker_joblist.html',{'jobm':job,'categories':categories,'e':e,'li':li})
   
def terms_and_condition_job(request):
    return render(request,'terms_and_condition_job.html')   