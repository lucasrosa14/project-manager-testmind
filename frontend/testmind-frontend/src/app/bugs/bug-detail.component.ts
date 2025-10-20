import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BugService, Bug } from '../bug.service';
import { ActivatedRoute, RouterModule } from '@angular/router';

@Component({
  selector: 'app-bug-detail',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './bug-detail.component.html'
})
export class BugDetailComponent implements OnInit {
  bug: Bug | null = null;

  constructor(private bugService: BugService, private route: ActivatedRoute) {}

  ngOnInit(): void {
    const id = +this.route.snapshot.params['id'];
    this.bugService.get(id).subscribe(data => this.bug = data);
  }
}
