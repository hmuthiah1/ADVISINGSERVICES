from django.contrib import admin
from .models import College, Department, Degree, Course, CurriculumGuide, DegreeChecklist, DegreeChecklistPdf

# Register your models here.
myModels = [College, Department, Degree, Course, CurriculumGuide, DegreeChecklist, DegreeChecklistPdf]  # iterable list
admin.site.register(myModels)