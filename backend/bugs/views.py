from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import BugForm
from .models import Bug
from projects.models import Project

@login_required
def bug_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.user.role not in ['admin', 'consultor']:
        return redirect('project_detail', pk=project_pk)
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save(project=project, user=request.user)
            return redirect('project_detail', pk=project_pk)
    else:
        form = BugForm()
    return render(request, 'bugs/bug_form.html', {'form': form, 'project': project})
