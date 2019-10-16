from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Employee)
admin.site.register(EmployeeType)
admin.site.register(Location)
admin.site.register(Department)
admin.site.register(AssetMaster)
admin.site.register(Ticket)