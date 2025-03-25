from django.urls import path
from . import views 
from .views import GeneratePdf
urlpatterns=[ 
    path('jobseeker_joblist/',views.jobseeker_joblist,name='jobseeker_joblist'),
    path('terms_and_condition_job/',views.terms_and_condition_job,name='terms_and_condition_job'),
    path('jobseeker_profile/',views.jobseeker_profile,name='jobseeker_profile'),
    path('j_jobdetails/<int:myid>',views.j_jobdetails,name='j_jobdetails'),
    path('jobseeker_search/',views.jobseeker_search,name='jobseeker_search'),
    path('jobseeker_saved_jobs/',views.jobseeker_saved_jobs,name='jobseeker_saved_jobs'),
    path('jobseeker_change_pass/',views.jobseeker_change_pass,name='jobseeker_change_pass'),
    path('jobseeker_create_cv/',views.jobseeker_create_cv,name='jobseeker_create_cv'),
    path('jobseeker_applied_job/',views.jobseeker_applied_job,name='jobseeker_applied_job'),
    path('apply_job/<int:pid>',views.apply_job,name='apply_job'),
    path('resume_page/',views.resume_page,name='resume_page'),
    path('pdf/', GeneratePdf.as_view(),name='pdf'), 
   
   
  
  
    
]