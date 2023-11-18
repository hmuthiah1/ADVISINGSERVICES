from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resources import *
from .models import *
    
# Register your models here.

@admin.register(College)
class CollegeAdmin(ImportExportModelAdmin):
    resource_class  =   CollegeAdminResource
    list_display = ['CollegeID', 'College']

@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    resource_class  =   DepartmentAdminResource
    list_display = ['DepartmentID', 'DepartmentName', 'CollegeID']

@admin.register(Degree)
class DegreeAdmin(ImportExportModelAdmin):
    resource_class  =   DegreeAdminResource
    list_display = ['DegreeID', 'DegreeName', 'DepartmentID']

@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    resource_class  =   CourseAdminResource
    list_display = ['CourseID', 'CourseName', 'Hrs', 'DegreeID']

@admin.register(CurriculumGuide)
class CurriculumGuidAdmin(ImportExportModelAdmin):
    resource_class  =   CurriculumGuideAdminResource
    list_display = ['DegreeID', 'FiscalYear', 'RowID', 'YearNumber', 'Semester', 'CourseInstruction', 'Hrs']

@admin.register(DegreeChecklist)
class DegreeChecklistAdmin(ImportExportModelAdmin):
    resource_class  =   DegreeChecklistAdminResource
    list_display = ['DegreeID', 'FiscalYear', 'RowID', 'RequirementGroup', 'RequirementSubGroup', 'CourseInstruction', 'Hrs']

@admin.register(DegreeChecklistPdf)
class DegreeChecklistPdfAdmin(ImportExportModelAdmin):
    resource_class  =   DegreeChecklistPdfAdminResource
    list_display = ['DegreeID', 'FiscalYear', 'pdf']