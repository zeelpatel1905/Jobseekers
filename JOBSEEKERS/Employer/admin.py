from django.contrib import admin
from .models import Employee, Dept, Designation, Company, Company_service
# Register your models here.

admin.site.register(Employee)
admin.site.register(Dept)
admin.site.register(Designation)
admin.site.register(Company)
admin.site.register(Company_service)

