from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from .models import College
from .models import Department
from .models import Degree
from .models import Course
from .models import CurriculumGuide
from .models import DegreeChecklist
from .models import DegreeChecklistPdf
from .forms import CollegeForm
from .forms import CurriculumForm
from .forms import DegreeChecklistPdfForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets

# Create your views here.
def home(request):
    return render(request, 'home.html',
    {
            "title": "Student Advising Service"
        }
    )

def all_college(request):
    college_list = College.objects.all().order_by('CollegeID')
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

def add_college(request):
    submitted = False
    if request.method == 'POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-college?submitted=True')
    else:
        form = CollegeForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'add_college.html', 
        {
            'form': form,
            'submitted': submitted,
            "title": "Add College to Database"
            }
    )

def add_curriculum(request):
    submitted = False
    if request.method == 'POST':
        form = CurriculumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-curriculum?submitted=True')
    else:
        form = CurriculumForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'add_curriculum.html', 
        {
            'form': form,
            'submitted': submitted,
            "title": "Add Curriculum to Database"
            }
    )

def DegreeChecklistPdf_view(request):
    DegreeChecklistPdfs = DegreeChecklistPdf.objects.all() 
    return render(request,'DegreeChecklistPdf_view.html', 
    {
        'DegreeChecklistPdfs' : DegreeChecklistPdfs,
        "title": "View all DegreeChecklist"
        }
    )

def DegreeChecklistPdf_upload(request):
    if request.method == 'POST':
        form = DegreeChecklistPdfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('DegreeChecklistPdf-view')
    else:
        form = DegreeChecklistPdfForm()
        return render(request,'DegreeChecklistPdf_upload.html', 
            {
                'form': form,
                "title": "Upload DegreeChecklist in pdf"
                }
    )

# Create API view
class CollegeApiView(APIView):
    serializer_class = CollegeSerailizer
    def get(self,request):
        allColleges= College.objects.all().values()
        return Response({"Message":"List of Colleges", "College List":allColleges})

    def post(self,request):
            #print('Request data is : ', request.data)
            serializers_obj=CollegeSerailizer(data=request.data)
            if(serializers_obj.is_valid()):
                College.objects.create(CollegeID=serializers_obj.data.get("CollegeID"),
                    College=serializers_obj.data.get("College"),
                )
                NewCollege = College.objects.all().filter(CollegeID=request.data["CollegeID"]).values()
                return Response({"Message":"New College Added!", "New College":NewCollege})   
            else:
                return Response(serializers_obj.errors)  

class CurriculumViewSet(viewsets.ModelViewSet):
    queryset = CurriculumGuide.objects.all()
    serializer_class = CurriculumSerailizer