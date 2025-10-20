import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ClientService, Client } from '../client.service';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-client-list',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './client-list.component.html'
})
export class ClientListComponent implements OnInit {
  clients: Client[] = [];
  loading = true;
  error = '';

  constructor(private clientService: ClientService) {}

  ngOnInit(): void {
    this.fetchClients();
  }

  fetchClients() {
    this.clientService.list().subscribe({
      next: data => {
        this.clients = data;
        this.loading = false;
      },
      error: () => {
        this.error = 'Erro ao carregar clientes';
        this.loading = false;
      }
    });
  }

  deleteClient(id: number) {
    if (confirm('Deseja realmente excluir este cliente?')) {
      this.clientService.delete(id).subscribe(() => {
        this.clients = this.clients.filter(c => c.id !== id);
      }, () => alert('Não foi possível excluir este cliente.'));
    }
  }
}
