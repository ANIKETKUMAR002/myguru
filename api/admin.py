from django.contrib import admin
from .models import Student_management, Aptitude_category_management,Aptitude_test_management,Question,Result

# Register your models here.
admin.site.register(Student_management)
admin.site.register(Aptitude_category_management)
admin.site.register(Aptitude_test_management)
admin.site.register(Question)
admin.site.register(Result)