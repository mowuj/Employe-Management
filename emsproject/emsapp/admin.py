from django.contrib import admin
from .models import *
# Register your models here.

class DistrictAdmin(admin.ModelAdmin):
    model=District
    list_display = ['name','division']

class EmployeeAdmin(admin.ModelAdmin):
    model=Employee
    list_display = ['username',
                    'department',
                    'district','full_name',
                    'email','phone'
                    ,'father_name',
                    'mother_name']


class LeaveAdmin(admin.ModelAdmin):
    model=District
    list_display = ['user',
                    'cause_of_leave',
                    'start_date',
                    'end_date',
                    'check_status',
                    'approve_status']
    list_editable = ['check_status','approve_status']

class HolidayAdmin(admin.ModelAdmin):
    model=District
    list_display = ['Description','start_date','Description']

class DailyTaskAdmin(admin.ModelAdmin):
    model=DailyTask 
    list_display = ['user',
                    'title',
                    'description',
                    'working_status',
                    'do_status',
                    'done_status']

admin.site.register(Department)
admin.site.register(Division)
admin.site.register(Post)
admin.site.register(Meeting)
admin.site.register(District,DistrictAdmin)
admin.site.register(Leave,LeaveAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Holiday,HolidayAdmin)
admin.site.register(DailyTask,DailyTaskAdmin)
admin.site.register(Attendence)
admin.site.register(Client)
