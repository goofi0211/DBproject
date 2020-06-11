from django.contrib import admin
from .models import Employee
# Register your models here.
#admin filter
class employeeAdmin(admin.ModelAdmin):
    list_display=('name','salary','job_title','published_date','boss')
    #list_filter=('name','salary',)
    search_fields=('name','salary',)
    ordering=('id',)

admin.site.register(Employee,employeeAdmin)