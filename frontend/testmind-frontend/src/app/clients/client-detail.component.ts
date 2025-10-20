import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ClientService, Client } from '../client.service';
import { ActivatedRoute, RouterModule } from '@angular/router';

@Component({
  selector: 'app-client-detail',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './client-detail.component.html'
})
export class ClientDetailComponent implements OnInit {
  client: Client | null = null;

  constructor(private clientService: ClientService, private route: ActivatedRoute) {}

  ngOnInit(): void {
    const id = +this.route.snapshot.params['id'];
    this.clientService.get(id).subscribe(data => this.client = data);
  }
}
