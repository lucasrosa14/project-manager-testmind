import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BugService, Bug } from '../bug.service';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-bug-list',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './bug-list.component.html'
})
export class BugListComponent implements OnInit {
  bugs: Bug[] = [];
  loading = true;
  error = '';

  constructor(private bugService: BugService) {}

  ngOnInit(): void {
    this.fetchBugs();
  }

  fetchBugs() {
    this.bugService.list().subscribe({
      next: data => {
        this.bugs = data;
        this.loading = false;
      },
      error: () => {
        this.error = 'Erro ao carregar bugs';
        this.loading = false;
      }
    });
  }

  deleteBug(id: number) {
    if (confirm('Deseja realmente excluir este bug?')) {
      this.bugService.delete(id).subscribe(() => {
        this.bugs = this.bugs.filter(b => b.id !== id);
      }, () => alert('Não foi possível excluir este bug.'));
    }
  }
}
