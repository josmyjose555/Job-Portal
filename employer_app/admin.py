from django.contrib import admin
from .models import AppliedList, Joblist, Jobtype,Experience,Category
# Register your models here.
admin.site.register(Jobtype)
admin.site.register(Experience)
admin.site.register(Category)
class JoblistAdmin(admin.ModelAdmin):
    list_display=('id','company','j_title','owner','type','location','no_of_vacancy','category','last_date')

admin.site.register(Joblist,JoblistAdmin)
class ApplyAdmin(admin.ModelAdmin):
  
    list_display=('id','getname','job','get_company','resume','get_contact','apply_date','status')
    def getname(self,obj):
        return obj.candidate.user.first_name +' ' +obj.candidate.user.last_name
    getname.short_description = 'Name Of Applicant' 
    def get_company(self,obj):
        return obj.job.company
    get_company.short_description = 'Company' 
    def get_contact(self,obj):
        return obj.candidate.user.email
    get_contact.short_description = 'Email' 

admin.site.register(AppliedList,ApplyAdmin)