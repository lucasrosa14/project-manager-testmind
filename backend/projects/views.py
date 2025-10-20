from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse

@login_required
def project_list(request):
    if request.user.role == 'consultor':
        projects = Project.objects.all()  # Consultor vê todos os projetos
    else:
        projects = Project.objects.all()  # Admin vê todos
    return render(request, 'projects/project_list.html', {'projects': projects})

@login_required
def project_create(request):
    if request.user.role != 'admin':
        return redirect('project_list')
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.instance.criado_por = request.user
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

@login_required
def project_concluir(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.status_projeto = 'CONCLUIDO'
    project.save()
    return redirect('project_detail', pk=pk)

@login_required
def project_cancelar(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.status_projeto = 'CANCELADO'
    project.save()
    return redirect('project_detail', pk=pk)

@require_POST
def concluir_projeto(request, project_id):
    projeto = get_object_or_404(Project, id=project_id)
    projeto.status = "Concluído"
    projeto.end_date = timezone.now().date()
    projeto.save()
    return JsonResponse({"message": f"Projeto '{projeto.name}' marcado como concluído."})


@require_POST
def cancelar_projeto(request, project_id):
    projeto = get_object_or_404(Project, id=project_id)
    projeto.status = "Cancelado"
    projeto.save()
    return JsonResponse({"message": f"Projeto '{projeto.name}' cancelado."})