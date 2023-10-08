from django.contrib import admin
from .models import College, Department, Degree, Course, CurriculumGuide, DegreeChecklist

# Register your models here.
myModels = [College, Department, Degree, Course, CurriculumGuide, DegreeChecklist]  # iterable list
admin.site.register(myModels)