from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from jobseeker_app.models import Resume



from .models import Employer, Jobseeker
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from employer_app.models import Joblist,Category,AppliedList
import re
# employer register
def employer_register(request):
    if request.method=='POST':
        c_name=request.POST['company_name']
        name=request.POST['company_user_name']
        email=request.POST['company_email']
        password1=request.POST['upassword']
        password2=request.POST['cpassword']
        contact=request.POST['mobile']
        designation=request.POST['company_user_designation']
        lo=request.FILES['clogo']
        
        if len(contact)>10 or len(contact)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/register/employer_register')
        if not contact.isdigit():
            messages.info(request,"Enter a valid Contact Number")
            return redirect('/register/employer_register')

        if len(password1)<8 or len(password1)>20:
            messages.info(request,"Password must be 8 Characters")
            return redirect('/register/employer_register')
        

        if password1 != password2:
            messages.info(request, "Passwords do not match.")
            return redirect('/register/employer_register')
        if email:
            if re.match('\w[\w\.-]*@\w[\w\.-]+\.\w+', email) == None:
                messages.info(request,"Enter a valid Email")
                return redirect('/register/employer_register')
        try:
            if User.objects.get(username=email):
                messages.warning(request,"Email Id is Taken")
                return redirect('/register/employer_register')
           
        except Exception as identifier:
            pass
        
        
        try:
            if Employer.objects.get(mobile=contact):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/register/employer_register')
           
        except Exception as identifier:
            pass
        user=User.objects.create_user(username=email,password=password1)
        employer=Employer.objects.create(user=user,name=name,mobile=contact,company=c_name,designation=designation,image=lo,type="employer",status='pending')
        user.save();
        employer.save();
        messages.success(request,'employer registration is sucessful!, Please Login')
        return redirect('/register/employer_login/')
            
       
    return render(request,'employer_register.html')
def employer_login(request):
    if request.method=='POST':
        username=request.POST['user_email']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            try:
                user1=Employer.objects.get(user=user)
                if user1.type=='employer':

                    login(request,user)
                    
                    
                    return redirect('/employer/company_profile/')
                else:
                    messages.error(request,'User Not Found')
                    return redirect('/register/employer_login')
                   
            except:
                pass

        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/register/employer_login')
       
                
    return render(request,'employer_login.html')
def employer_logout(request):
    logout(request)
    messages.success(request,'Logged out successfully') 
    return redirect('/register/employer_login')
# user Register
def jobseeker_register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['user_email']
        mobile=request.POST['user_mobile']
        pwd1=request.POST['user_password']
        pwd2=request.POST['user_confirm_password']
    
        if len(mobile)>10 or len(mobile)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/register/jobseeker_register')
        if len(pwd1)<8 or len(pwd1)>20:
            messages.info(request, "Password must be 8 character")
            return redirect('/register/jobseeker_register')
        if not mobile.isdigit():
            messages.info(request, "Enter a valid number")
            return redirect('/register/jobseeker_register')


        
        if pwd1 != pwd2:
            messages.info(request, "Passwords do not match.")
            return redirect('/register/jobseeker_register')
        if email:
            if re.match('\w[\w\.-]*@\w[\w\.-]+\.\w+', email) == None:
                messages.info(request,"Enter a valid Email")
                return redirect('/register/jobseeker_register')
        try:
            if User.objects.get(username=email):
                messages.warning(request,"Email Id is Taken")
                return redirect('/register/jobseeker_register')
           
        except Exception as identifier:
            pass
        
        
        try:
            if Employer.objects.get(mobile=mobile):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/register/jobseeker_register')
           
        except Exception as identifier:
            pass


        user=User.objects.create_user(username=email,password=pwd1,first_name=first_name,last_name=last_name,email=email)
        jobseeker=Jobseeker.objects.create(user=user,mobile=mobile,type="jobseeker",status='pending')
        user.save();
        jobseeker.save();
        messages.success(request,'Jobseeeker registration is sucessful!, Please Login')
        return redirect('/register/jobseeker_login/')





    return render(request,'jobseeker_register.html')




def jobseeker_login(request):
    if request.method=='POST':
        username=request.POST['user_email']
        password=request.POST['user_password']
        user=authenticate(username=username,password=password)
        if user is not None:
            try:
                user1=Jobseeker.objects.get(user=user)
                
                if user1.type=='jobseeker':

                    login(request,user)
                   

            
                    return redirect('/register/jobseeker_home')
                else:
                    messages.error(request,"User Not Found")
                    return redirect('/')
            except:
                pass
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/register/jobseeker_login')
    return render(request,'jobseeker_login.html')
def employer_home(request):
    p=Resume.objects.all().order_by('-id')

    return render(request,'employer_home.html',{'p':p})
def jobseeker_home(request):
    categories=Category.objects.all()
    job=Joblist.objects.all().order_by('-id')[0:6]
    user=request.user


    jobseeker=Jobseeker.objects.get(user=user)
    data=AppliedList.objects.filter(candidate=jobseeker)
    li=[]
    for i in data:
        li.append(i.job.id)
    return render(request,'jobseeker_home.html',{'job':job,'categories':categories,'li':li})
def jobseeker_logout(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('/register/jobseeker_login')
