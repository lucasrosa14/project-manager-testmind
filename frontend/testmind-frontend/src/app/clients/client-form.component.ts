import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ClientService, Client } from '../client.service';
import { Router, ActivatedRoute, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-client-form',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './client-form.component.html'
})
export class ClientFormComponent implements OnInit {
  client: Partial<Client> = {};
  isEdit = false;
  id: number | null = null;

  constructor(private clientService: ClientService, private router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      if (params['id']) {
        this.isEdit = true;
        this.id = +params['id'];
        this.clientService.get(this.id).subscribe(data => this.client = data);
      }
    });
  }

  save() {
    if (this.isEdit && this.id) {
      this.clientService.update(this.id, this.client).subscribe(() => this.router.navigate(['/clients']));
    } else {
      this.clientService.create(this.client).subscribe(() => this.router.navigate(['/clients']));
    }
  }
}
