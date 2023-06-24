from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.all_projects, name='allProjects'),
    path('<int:project_id>', views.project_detail, name='project_detail'),


]