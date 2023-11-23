from django.db import models

# Create your models here.

class College(models.Model):
    CollegeID = models.CharField(max_length=50, primary_key=True)
    College = models.CharField(max_length=200)
    def __str__(self):
        return str(self.CollegeID)

    @property
    def total_college(self):
        total_college = College.objects.filter(CollegeID=self)
        return total_college.count()

class Department(models.Model):
    DepartmentID = models.CharField(max_length=50, primary_key=True)
    DepartmentName = models.CharField(max_length=200)
    CollegeID = models.ForeignKey(College, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.DepartmentID)

class Degree(models.Model):
    DegreeID = models.CharField(max_length=50, primary_key=True)
    DegreeName = models.CharField(max_length=200)
    DepartmentID = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.DegreeID)

class Course(models.Model):
    CourseID = models.CharField(max_length=50)
    CourseName = models.CharField(max_length=200)
    Hrs = models.IntegerField()
    DegreeID = models.ForeignKey(Degree, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.CourseID)
   
class CurriculumGuide(models.Model):
    DegreeID = models.ForeignKey(Degree, on_delete=models.CASCADE)
    FiscalYear = models.CharField(max_length=20)
    RowID = models.IntegerField()
    YearNumber = models.IntegerField()
    Semester = models.CharField(max_length=20)
    CourseInstruction = models.CharField(max_length=500)
    Hrs = models.IntegerField()
    def __str__(self):
        return str(self.DegreeID)

    class Meta:
        unique_together = (('DegreeID', 'FiscalYear','RowID'),)

class DegreeChecklist(models.Model):
    DegreeID = models.ForeignKey(Degree, on_delete=models.CASCADE)
    FiscalYear = models.CharField(max_length=20)
    RowID = models.IntegerField()
    RequirementGroup = models.CharField(max_length=200)
    RequirementSubGroup = models.CharField(max_length=200)
    CourseInstruction = models.CharField(max_length=500)
    Hrs = models.IntegerField()
    def __str__(self):
        return str(self.DegreeID)

    class Meta:
        unique_together = (('DegreeID', 'FiscalYear','RowID'),)

class DegreeChecklistPdf(models.Model):
    DegreeID = models.ForeignKey(Degree, on_delete=models.CASCADE)
    FiscalYear = models.CharField(max_length=20)
    pdf = models.FileField(upload_to='DegreeChecklist/pdfs/')
    def __str__(self):
        return str(self.DegreeID)