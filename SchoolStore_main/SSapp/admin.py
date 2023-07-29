from django.contrib import admin
from .models import Department,Courses,Purposes,StudentForm,Review

# Register your models here.
admin.site.register(Department)
admin.site.register(Courses)
admin.site.register(Purposes)
admin.site.register(StudentForm)
admin.site.register(Review)
