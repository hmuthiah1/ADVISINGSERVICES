from django.db import models

# Create your models here.


class College(models.Model):
    CollegeID = models.CharField(max_length=50, primary_key=True)
    College = models.CharField(max_length=200)

class Department(models.Model):
    DepartmentID = models.CharField(max_length=50, primary_key=True)
    DepartmentName = models.CharField(max_length=200)
    CollegeID = models.ForeignKey(College, on_delete=models.CASCADE)

class Degree(models.Model):
    DegreeID = models.CharField(max_length=50, primary_key=True)
    DegreeName = models.CharField(max_length=200)
    DepartmentID = models.ForeignKey(Department, on_delete=models.CASCADE)

class Course(models.Model):
    CourseID = models.CharField(max_length=50)
    CourseName = models.CharField(max_length=200)
    Hrs = models.IntegerField()
    DegreeID = models.ForeignKey(Degree, on_delete=models.CASCADE)

class CurriculumGuide(models.Model):
    DegreeID = models.ForeignKey(Degree, on_delete=models.CASCADE)
    FiscalYear = models.CharField(max_length=20)
    RowID = models.IntegerField()
    YearNumber = models.IntegerField()
    Semester = models.CharField(max_length=20)
    CourseInstruction = models.CharField(max_length=500)
    Hrs = models.IntegerField()

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

    class Meta:
        unique_together = (('DegreeID', 'FiscalYear','RowID'),)