from django.shortcuts import render, get_object_or_404
from .models import Project
from .forms import ProjectFilter


# Create your views here.
def all_projects(request):
    projects = Project.objects.all()
    filtered = ProjectFilter(request.GET, queryset=projects)
    projects = filtered.qs

    context = {
        'projects': projects,
        'filtered': filtered,

    }
    return render(request, 'allprojects.html', context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    context = {
        'project': project
    }
    return render(request, 'projectdetail.html', context)
