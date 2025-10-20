import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProjectService, Project } from '../project.service';
import { RouterModule, Router } from '@angular/router';

@Component({
  selector: 'app-project-list',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './project-list.component.html'
})
export class ProjectListComponent implements OnInit {
  projects: Project[] = [];
  loading = true;
  error = '';

  constructor(private projectService: ProjectService, private router: Router) {}

  ngOnInit(): void {
    this.fetchProjects();
  }

  fetchProjects(): void {
    this.projectService.list().subscribe({
      next: (data) => {
        this.projects = data;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Erro ao carregar projetos';
        this.loading = false;
      }
    });
  }

  deleteProject(id: number) {
    if (confirm('Tem certeza que deseja excluir este projeto?')) {
      this.projectService.delete(id).subscribe(() => {
        this.projects = this.projects.filter(p => p.id !== id);
      }, () => alert('Não foi possível excluir o projeto.'));
    }
  }
}
