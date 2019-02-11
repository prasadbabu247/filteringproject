from django.contrib import admin
from pageapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)
# Register your models here.
