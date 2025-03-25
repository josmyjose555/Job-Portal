from django.urls import path
from .import views
urlpatterns=[ 
    path('employer_postjob/',views.employer_postjob,name='employer_postjob'),
    path('edit_job/<int:pid>/',views.edit_job,name='edit_job'),
    path('company_profile/',views.company_profile,name='company_profile'),
    path('serach_cv/',views.search_cv,name='search_cv'),
    path('employer_change_password',views.employer_change_password,name='employer_change_password'),
    path('employer_manager_job/',views.employer_manage_job,name='employer_manage_job'),
    path('delete_job/<int:did>',views.delete_job,name='delete_job'),
    path('manage_candidate/',views.manage_candidate,name='manage_candidate'),
    path('approve_candidate/<int:id>/',views.approve_candidate,name='approve_candidate'),
    path(' reject_candidate/<int:id>/',views.reject_candidate,name=' reject_candidate'),
    path('view_candidate/<int:id>/',views.view_candidate,name='view_candidate'),
    path('shorlisted_candidate/<int:id>/',views.shorlisted_candidate,name='shorlisted_candidate'),
    path('machine_test/<int:id>/',views.machine_test,name='machine_test'),
    path('interview/<int:id>/',views.interview,name='interview'),
    path('edit_company/<int:cid>/',views.edit_company,name='edit_company'),
    path('edit_logo/<int:cid>/',views.edit_logo,name='edit_logo')
    
]