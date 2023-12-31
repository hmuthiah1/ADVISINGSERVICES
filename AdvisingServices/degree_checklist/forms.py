from django import forms
from django.forms import ModelForm
from .models import College
from .models import CurriculumGuide
from .models import DegreeChecklistPdf 
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit 

# Create a college form
class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = ('CollegeID', 'College')
        labels = {
            'CollegeID': '',
            'College': '',            
        }
        widgets = {
            'CollegeID': forms.TextInput(attrs={'class': 'form-control','placeholder': 'College ID'}),
            'College': forms.TextInput(attrs={'class': 'form-control','placeholder': 'College Name'}),
        }

# Create a curriculum form
class CurriculumForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = CurriculumGuide
        fields = ('DegreeID', 'FiscalYear', 'RowID', 'YearNumber', 'Semester', 'CourseInstruction', 'Hrs')
        labels = {
            'DegreeID': '',
            'FiscalYear': '',        
            'RowID': '',
            'YearNumber': '',  
            'Semester': '',
            'CourseInstruction': '',  
            'Hrs': '',    
        }
        widgets = {
            'DegreeID': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Degree ID'}),
            'FiscalYear': forms.TextInput(attrs={'class': 'form-control','placeholder': 'FiscalYear'}),
            'RowID': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Row ID'}),
            'YearNumber': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Year Number'}),
            'Semester': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Semester'}),
            'CourseInstruction': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Course Instruction'}),
            'Hrs': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Hours'}),
        }      

# Create a DegreeChecklistPdf form
class DegreeChecklistPdfForm(ModelForm):
    class Meta:
        model = DegreeChecklistPdf
        fields = ('DegreeID', 'FiscalYear', 'pdf')