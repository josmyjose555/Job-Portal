from django.contrib import admin

from jobseeker_app.models import Resume

# Register your models here.
class ResumeAdmin(admin.ModelAdmin):
    list_display=('id','owner','first_name','last_name','create_date')
admin.site.register(Resume,ResumeAdmin)