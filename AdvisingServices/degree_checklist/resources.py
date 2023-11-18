from import_export import resources
from .models import *

class CollegeAdminResource(resources.ModelResource):

    class Meta:
        model   =   College
        exclude = ('id',)
        import_id_fields = ['CollegeID', ]
        fields = ['CollegeID', 'College']

class DepartmentAdminResource(resources.ModelResource):

    class Meta:
        model   =   Department
        exclude = ('id',)
        import_id_fields = ['DepartmentID', ]
        fields = ['DepartmentID', 'DepartmentName', 'CollegeID']

class DegreeAdminResource(resources.ModelResource):

    class Meta:
        model   =   Degree
        exclude = ('id',)
        import_id_fields = ['DegreeID', ]
        fields = ['DegreeID', 'DegreeName', 'DepartmentID']

class CourseAdminResource(resources.ModelResource):

    class Meta:
        model   =   Course
        exclude = ('id',)
        import_id_fields = ['CourseID', ]
        fields = ['CourseID', 'CourseName', 'Hrs', 'DegreeID']

class CurriculumGuideAdminResource(resources.ModelResource):

    class Meta:
        model   =   CurriculumGuide
        exclude = ('id',)
        import_id_fields = ['DegreeID', 'FiscalYear','RowID', ]
        fields = ['DegreeID', 'FiscalYear', 'RowID', 'YearNumber', 'Semester', 'CourseInstruction', 'Hrs']

class DegreeChecklistAdminResource(resources.ModelResource):

    class Meta:
        model   =   DegreeChecklist
        exclude = ('id',)
        import_id_fields = ['DegreeID', 'FiscalYear','RowID', ]
        fields = ['DegreeID', 'FiscalYear', 'RowID', 'RequirementGroup', 'RequirementSubGroup', 'CourseInstruction', 'Hrs']

class DegreeChecklistPdfAdminResource(resources.ModelResource):

    class Meta:
        model   =   DegreeChecklistPdf
        exclude = ('id',)
        import_id_fields = ['DegreeID', 'FiscalYear', ]
        fields = ['DegreeID', 'FiscalYear', 'pdf']