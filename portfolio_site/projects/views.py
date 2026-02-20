from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Project
from .forms import ProjectForm

def home(request):
    featured_projects = Project.objects.all().order_by('-created_at')[:3]
    return render(request, 'home.html', {'projects': featured_projects})

def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    tech_list = [t.strip() for t in project.tech_stack.split(',')]
    return render(request, 'projects/project_detail.html', {'project': project, 'tech_list': tech_list})

# Admin/Superuser Only Views
def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project created successfully!')
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form, 'title': 'Add New Project'})

@login_required
@user_passes_test(is_admin)
def edit_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated!')
            return redirect('project_detail', slug=project.slug)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form, 'title': 'Edit Project'})

@login_required
@user_passes_test(is_admin)
def delete_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted.')
        return redirect('dashboard')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})