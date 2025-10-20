import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProjectService, Project } from '../project.service';
import { ClientService, Client } from '../../clients/client.service';
import { Router, ActivatedRoute, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-project-form',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './project-form.component.html'
})
export class ProjectFormComponent implements OnInit {
  project: Partial<Project> = {};
  clients: Client[] = [];
  isEdit = false;
  id: number | null = null;

  constructor(
    private projectService: ProjectService,
    private clientService: ClientService,
    private router: Router,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.clientService.list().subscribe(data => this.clients = data);
    this.route.params.subscribe(params => {
      if (params['id']) {
        this.isEdit = true;
        this.id = +params['id'];
        this.projectService.get(this.id).subscribe(data => this.project = data);
      }
    });
  }

  save() {
    if (this.isEdit && this.id) {
      this.projectService.update(this.id, this.project).subscribe(() => this.router.navigate(['/projects']));
    } else {
      this.projectService.create(this.project).subscribe(() => this.router.navigate(['/projects']));
    }
  }
}
