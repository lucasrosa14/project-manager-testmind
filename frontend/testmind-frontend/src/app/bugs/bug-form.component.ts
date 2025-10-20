import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BugService, Bug } from '../bug.service';
import { ProjectService, Project } from '../../projects/project.service';
import { Router, ActivatedRoute, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-bug-form',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './bug-form.component.html'
})
export class BugFormComponent implements OnInit {
  bug: Partial<Bug> = {};
  projects: Project[] = [];
  isEdit = false;
  id: number | null = null;

  constructor(
    private bugService: BugService,
    private projectService: ProjectService,
    private router: Router,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.projectService.list().subscribe(data => this.projects = data);

    this.route.params.subscribe(params => {
      if (params['id']) {
        this.isEdit = true;
        this.id = +params['id'];
        this.bugService.get(this.id).subscribe(data => this.bug = data);
      }
    });
  }

  save() {
    if (this.isEdit && this.id) {
      this.bugService.update(this.id, this.bug).subscribe(() => this.router.navigate(['/bugs']));
    } else {
      this.bugService.create(this.bug).subscribe(() => this.router.navigate(['/bugs']));
    }
  }
}
