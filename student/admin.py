from django.contrib import admin

# Register your models here.
from .models import *

class my_student_detail(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'upload')

admin.site.register(Student_detail, my_student_detail)


admin.site.register(Mark)




