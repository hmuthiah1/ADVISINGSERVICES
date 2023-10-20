from django import forms
from django.forms import ModelForm
from .models import College
from .models import CurriculumGuide

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