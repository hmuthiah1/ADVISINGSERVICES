from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('CurriculumGuideApi', views.CurriculumViewSet)

urlpatterns = [
    path("", views.home, name="home"),
    path('college', views.all_college, name="list-college"),
    path('department', views.all_department, name="list-department"),
    path('degree', views.all_degree, name="list-degree"),
    path('course', views.all_course, name="list-course"),
    path('curriculumguide', views.all_curriculum_guide, name="curriculum-guide"),
    path('degreechecklist', views.all_degree_checklist, name="degree-checklist"),
    path('add-college', views.add_college, name="add-college"),
    path('add-curriculum', views.add_curriculum, name="add-curriculum"),
    path('DegreeChecklistPdf-view', views.DegreeChecklistPdf_view, name="DegreeChecklistPdf-view"),
    path('DegreeChecklistPdf-upload', views.DegreeChecklistPdf_upload, name="DegreeChecklistPdf-upload"),
    path('CollegeApi', views.CollegeApiView.as_view(), name="CollegeApi"),
    path('',include(router.urls)),
]