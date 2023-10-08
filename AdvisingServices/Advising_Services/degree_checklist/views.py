from django.shortcuts import render, HttpResponse
from .models import College
from .models import Department
from .models import Degree
from .models import Course
from .models import CurriculumGuide
from .models import DegreeChecklist

# Create your views here.
def home(request):
    return render(request, 'base.html',
    {
            "title": "Student Advising Service"
        }
    )

def all_college(request):
    college_list = College.objects.all().order_by('College')
    return render(request, 'college.html', 
    {
        'college_list' : college_list,
        "title": "College"
        }
    )

def all_department(request):
    department_list = Department.objects.all().order_by('DepartmentName')
    return render(request, 'department.html', 
    {
        'department_list' : department_list,
        "title": "Department"
        }
    )

def all_degree(request):
    degree_list = Degree.objects.all().order_by('DegreeName')
    return render(request, 'degree.html', 
    {
        'degree_list' : degree_list,
        "title": "Degree"
        }
    )

def all_course(request):
    course_list = Course.objects.all().order_by('CourseName')
    return render(request, 'course.html', 
    {
        'course_list' : course_list,
        "title": "Course"
        }
    )

def all_curriculum_guide(request):
    curriculum_guide = CurriculumGuide.objects.all().order_by('DegreeID','FiscalYear','RowID')
    return render(request, 'curriculum_guide.html', 
    {
        'curriculum_guide' : curriculum_guide,
        "title": "CurriculumGuide"
        }
    )

def all_degree_checklist(request):
    degree_checklist = DegreeChecklist.objects.all().order_by('DegreeID','FiscalYear','RowID')
    return render(request, 'degree_checklist.html', 
    {
        'degree_checklist' : degree_checklist,
        "title": "DegreeChecklist"
        }
    )