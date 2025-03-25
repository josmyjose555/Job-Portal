from datetime import datetime
from email.mime import application
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.models import Employer
from .models import AppliedList, Category, Joblist
from .models import Jobtype
from .models import Experience

# Create your views here.
def employer_postjob(request):
    user=request.user
    emp=Employer.objects.get(user=user)
    types=Jobtype.objects.all()
    cat=Category.objects.all()
    exp=Experience.objects.all()
    if request.method=='POST':
        job_title=request.POST['job_title']
        job_type=request.POST['type']
        job_cate=request.POST['cate']
        job_loc=request.POST['location']
        min_s=request.POST['min_s']
        max_s=request.POST['max_s']
        skill=request.POST['skill']
        edu=request.POST['quali']
        exp=request.POST['exp']
        email=request.POST['email']
        mob=request.POST['mobile']
        vacancy=request.POST['vacancy']
        close_date=request.POST['close_date']
        j_desc=request.POST['j_desc']
        cname=request.POST['cname']
        website=request.POST['website']
        c_desc=request.POST['c_desc']
        logo=request.FILES['logo']
        owner=request.user.id
        # owner=User.objects.get(user_id=request.user.id)
        job1=Joblist.objects.create(
        owner_id=owner,
        j_title=job_title,
        company=cname,
        type_id=job_type,
        category_id=job_cate,
        location=job_loc,
        min_salary=min_s,
        max_salary=max_s,
        skills=skill,
        education=edu,
        email=email,mobile=mob,
        no_of_vacancy=vacancy,
        job_desc=j_desc,
        c_website=website,
        c_overview=c_desc,
        logo=logo,
        exp_id=exp,
        last_date=close_date,
        date_created=datetime.now())
        job1.save()
        return redirect('/employer/employer_manager_job')
    return render(request,'employer_post_job.html',{'type':types,'cat':cat,'exp':exp,'emp':emp})
def edit_job(request,pid):
    # type=Jobtype.objects.all()
    pjob=Joblist.objects.get(id=pid)
    if request.method=='POST':
        job_title=request.POST['job_title']
        # job_type=request.POST['type']
        # job_cate=request.POST['cate']
        job_loc=request.POST['location']
        min_s=request.POST['min_s']
        max_s=request.POST['max_s']
        skill=request.POST['skill']
        edu=request.POST['quali']
        # exp=request.POST['exp']
        email=request.POST['email']
        mob=request.POST['mobile']
        vacancy=request.POST['vacancy']
        close_date=request.POST['close_date']
        j_desc=request.POST['j_desc']
        cname=request.POST['cname']
        website=request.POST['website']
        c_desc=request.POST['c_desc']
        pjob.j_title=job_title
        pjob.company=cname

        # pjob.type_id=job_type


        pjob.location=job_loc
        pjob.min_salary=min_s
        pjob.max_salary=max_s
        pjob.skills=skill
        pjob.education=edu
        pjob.email=email
        pjob.mobile=mob
        pjob.no_of_vacancy=vacancy
        pjob.job_desc=j_desc
        pjob.c_website=website
        pjob.c_overview=c_desc
        pjob.save()
        # pjob.exp_id=exp,
       
       
        if close_date:
            pjob.last_date=close_date
            pjob.save()
        messages.success(request,'Job updated Successfully')
        return redirect('/employer/employer_manager_job')
        
    return render(request,'edit_job.html',{'pjob':pjob})
################################################# delete jobs########################################################

def delete_job(request,did):
    jobd=Joblist.objects.get(id=did)
    jobd.delete()
    messages.success(request,'Job Deleted Successfully')
    return redirect('/employer/employer_manager_job')
def company_profile(request):
    user=request.user
    emp=Employer.objects.get(user=user)
    return render(request,'company_profile.html',{'emp':emp})
def search_cv(request):
    return render(request,'search_cv.html')
def employer_change_password(request):
    error=""
    if request.method=='POST':
        c=request.POST['current_password']
        n=request.POST['user_new_password']
        if len(n)<8 or len(n)<20:
            messages.info(request,"password must contain 8 characters")
            # return redirect('/employer/employer_change_password/')
            return redirect("/employer/employer_change_password")
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

    return render(request,'employer_change_password.html',d)
def employer_manage_job(request):
    a=Joblist.objects.filter(owner=request.user)
    return render(request,'employer_manage_job.html',{'j':a})
    #########################################################################################

def manage_candidate(request):
    application=AppliedList.objects.all()
    return render(request,'manage_candidate.html',{'application':application})
    ################################################################################

def approve_candidate(request,id):
    application=AppliedList.objects.get(id=id)
    application.status='Accept'
    application.save()
    return redirect('/employer/manage_candidate/')
def reject_candidate(request,id):
    application=AppliedList.objects.get(id=id)
    application.status='Reject'
    application.save()
    return redirect('/employer/manage_candidate/')
def view_candidate(request,id):
    application=AppliedList.objects.get(id=id)
    application.status='Viewed'
    application.save()
    return redirect('/employer/manage_candidate/') 
def shorlisted_candidate(request,id):
    application=AppliedList.objects.get(id=id)
    application.status='Shortlisted'
    application.save()
    return redirect('/employer/manage_candidate/')
def machine_test(request,id):
    application=AppliedList.objects.get(id=id)
    application.status='Machine Test'
    application.save()
    return redirect('/employer/manage_candidate/')
def interview(request,id):
    application=AppliedList.objects.get(id=id)
    application.status='Interview'
    application.save()
    # return render(request,'manage_candidate.html',{'application':application})
    return redirect('/employer/manage_candidate/')

def edit_company(request,cid):
    co=Employer.objects.get(id=cid)
    if request.method=='POST':
        company_name=request.POST['cname']
        cadd=request.POST['cadd']
        ccity=request.POST['ccity']
        cdis=request.POST['cdis']
        cpin=request.POST['cpin']
        cst=request.POST['cst']
        cco=request.POST['cco']
        web=request.POST['web']
        cemail=request.POST['cemail']
        cmobile=request.POST['cmobile']
        cyear=request.POST['cyear']
        cemp=request.POST['cemp']
        cdes=request.POST['cdes']
        # clogo=request.FILES['logo'].read()
        co.company=company_name
        co.address=cadd
        co.city=ccity
        co.district=cdis
        co.state=cst
        co.pin=cpin
        co.country=cco
        co.url=web
        co.user.username=cemail
        co.mobile=cmobile
        co.found_year=cyear
        co.no_of_employees=cemp
        co.comp_desc=cdes
        # co.image=clogo
        co.save();

        return redirect('/employer/company_profile/')
        

    return render(request,'edit_company.html',{'co':co})
    
def edit_logo(request,cid):
    co=Employer.objects.get(id=cid)
    if request.method=='POST':
        clogo=request.FILES['logo']
        co.image=clogo
        try:
            co.save()
            return redirect('/employer/company_profile/')
            
        except:
            pass
    return render(request,"edit_logo.html",{'co':co})
    

