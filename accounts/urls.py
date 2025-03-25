from django.urls import path
from . import views
urlpatterns=[ 
path('employer_home/',views.employer_home,name='employer_home'),
path('employer_register/',views.employer_register,name='employer_register'),
path('employer_login/',views.employer_login,name='employer_login'),
path('employer_logout/',views.employer_logout,name='employer_logout'),
path('jobseeker_home/',views.jobseeker_home,name='jobseeker_home'),
path('jobseeker_register/',views.jobseeker_register,name='jobseeker_register'),
path('jobseeker_login/',views.jobseeker_login,name='jobseeker_login'),
path('jobseeker_logout/',views.jobseeker_logout,name='jobseeker_logout')

]