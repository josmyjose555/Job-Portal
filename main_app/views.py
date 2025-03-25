from unicodedata import category
from django.shortcuts import render
from accounts.models import Employer, Jobseeker
from employer_app.models import Joblist,Category,Experience
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
# def error_404(request, exception):
#     return render(request, '404.html')
def index(request):
    categories=Category.objects.all()
    job=Joblist.objects.all().order_by('-id')[0:6]
    return render(request,'index.html',{'job':job,'categories':categories})


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
def terms_conditions(request):
    
    return render(request,'terms_conditions.html')
def privacy(request):
    return render(request,'privacy.html')
def faq(request):
    return render(request,'faq.html')
# all job list #########################################################################################################
def job_list(request):
    e=Experience.objects.all()
    h_joblist=Joblist.objects.all().order_by('-id')
    page=request.GET.get('page',1)
    paginator=Paginator(h_joblist,6)
    try:
        post=paginator.page(page)
    except PageNotAnInteger:
        post=paginator.page(1)
    except  EmptyPage:
        post=paginator.page(paginator.num_pages)

    return render(request,'joblist.html',{'h_joblist':post,'e':e})

############################################################################################################
def job_search(request):
    job=Joblist.objects.all()
    categories=Category.objects.all()
    e=Experience.objects.all()
    location=request.GET.get('location')
    categorys=request.GET.get('categorys')
    exp=request.GET.get('exp')
    sk=request.GET.get('sk')
    if location !=''  and  location is not None and sk !='' and sk is not None and exp !='' and exp is not None :   #(3 condition must satisfy (skill +location + experience))
        job=job.filter(Q(location__icontains=location) 
        & (Q(skills__icontains=sk) | Q(j_title__icontains=sk)| Q(education__icontains=sk))
        & Q(exp__e_title__icontains=exp)).distinct()

    elif location !=''  and  location is not None and sk !='' and sk is not None :   # (2 condition must location+ skill)
        job=job.filter(Q(location__icontains=location) 
        & (Q(skills__icontains=sk)| Q(j_title__icontains=sk) | Q(education__icontains=sk))).distinct()
        
    elif sk!='' and sk is not None and exp !='' and exp is not None:          # (2 condition must true  experience + skill)
        job=job.filter(Q(skills__icontains=sk) | Q(j_title__icontains=sk)| Q(education__icontains=sk)
        & Q(exp__e_title__icontains=exp)).distinct() 
    
    elif location !='' and location is not None:      # (only location )
        job=job.filter(location__icontains=location)
    
    elif categorys !='' and categorys is not None:    #(only category)
        job=job.filter(category__title=categorys)
    elif sk !='' and sk is not None:                # (search based on skills or company name or title )
        job=job.filter(Q(j_title__icontains=sk) | Q(skills__icontains=sk) |Q(company__icontains=sk) | Q(education__icontains=sk)).distinct()
    
    elif exp !='' and exp is not None:
        job=job.filter(exp__e_title__icontains=exp)




    return render(request,'joblist.html',{'h_joblist':job,'categories':categories,'e':e})

########################################################################################################################
# job details page
def h_jobdetails(request,myid):
    jobh=Joblist.objects.filter(pk=myid)
    return render(request,'h_jobdetails.html',{'jobh':jobh})


    