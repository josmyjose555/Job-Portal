from django.urls import path
from main_app import views
urlpatterns=[ 
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('joblist/',views.job_list,name='joblist'),
    path('contact/',views.contact,name='contact'),
    path('h_jobdetails/<int:myid>',views.h_jobdetails,name='h_jobdetails'),
    path('job_search/',views.job_search,name='job_search'),
    path('terms_conditions/',views.terms_conditions,name='terms_conditions'),
    path('privacy/',views.privacy,name='privacy'),
    path('faq',views.faq,name='faq')
    
]