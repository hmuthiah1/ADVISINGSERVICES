from django.test import SimpleTestCase
from django.urls import reverse, resolve
from degree_checklist.views import *


class TestUrls(SimpleTestCase):

    def test_college_url(self):
        url = reverse('list-college')
        self.assertEquals(resolve(url).func, all_college)

    def test_department_url(self):
        url = reverse('list-department')
        self.assertEquals(resolve(url).func, all_department)

    def test_degree_url(self):
        url = reverse('list-degree')
        self.assertEquals(resolve(url).func, all_degree)

    def test_course_url(self):
        url = reverse('list-course')
        self.assertEquals(resolve(url).func, all_course)

    def test_curriculum_guide_url(self):
        url = reverse('curriculum-guide')
        self.assertEquals(resolve(url).func, all_curriculum_guide)

    def test_degree_checklist_url(self):
        url = reverse('degree-checklist')
        self.assertEquals(resolve(url).func, all_degree_checklist)

    def test_add_college_url(self):
        url = reverse('add-college')
        self.assertEquals(resolve(url).func, add_college)        

    def test_add_curriculum_url(self):
        url = reverse('add-curriculum')
        self.assertEquals(resolve(url).func, add_curriculum)  

    def test_DegreeChecklistPdf_view_url(self):
        url = reverse('DegreeChecklistPdf-view')
        self.assertEquals(resolve(url).func, DegreeChecklistPdf_view)    

    def test_DegreeChecklistPdf_upload_url(self):
        url = reverse('DegreeChecklistPdf-upload')
        self.assertEquals(resolve(url).func, DegreeChecklistPdf_upload)  

    def test_CollegeApi_url(self):
        url = reverse('CollegeApi')
        self.assertEquals(resolve(url).func.view_class, CollegeApiView)         