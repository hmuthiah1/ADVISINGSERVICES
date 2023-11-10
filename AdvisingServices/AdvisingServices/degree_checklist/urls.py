from django.urls import path
from . import views

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
]