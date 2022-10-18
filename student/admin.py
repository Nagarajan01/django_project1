from django.contrib import admin

# Register your models here.
from .models import *

class my_student_detail(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll_number', 'upload', 'email')

admin.site.register(Student_detail, my_student_detail)

class my_mark(admin.ModelAdmin):
    list_display = ('id', 'roll_no', 'subject', 'mark',
     'Created_at', 'Modified_at', 'updated_by', 'created_by')

admin.site.register(Mark, my_mark)


from django.contrib import admin
from .models import bag, buyer



# Register your models here.
admin.site.register(bag)
admin.site.register(buyer)
# Register your models here.