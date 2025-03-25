import imp
from django.contrib import admin
from .models import Employer, Jobseeker
# Register your models here.
admin.site.site_header='IPSR Admin Dashboard'
admin.site.site_title="Welcome Admin"


class EmployerAdmin(admin.ModelAdmin):
    list_display=('id','user','name','company','designation','mobile','district','register_date')
    search_fields= ('company',)
admin.site.register(Employer,EmployerAdmin)

class JobseekerAdmin(admin.ModelAdmin):
    list_display=['id','get_name','get_email','mobile','register_date']
    def get_name(self,obj):
        return obj.user.first_name +' '+obj.user.last_name
    get_name.short_description = 'Name'     
    def get_email(self,obj):
        return obj.user.username
    get_email.short_description = 'Email' 
admin.site.register(Jobseeker,JobseekerAdmin)