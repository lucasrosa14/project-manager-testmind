import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Client {
  id: number;
  name: string;
  contact_email: string;
  contact_phone?: string;
}

@Injectable({
  providedIn: 'root'
})
export class ClientService {
  private apiUrl = '/api/clients/';

  constructor(private http: HttpClient) {}

  list(): Observable<Client[]> {
    return this.http.get<Client[]>(this.apiUrl);
  }

  get(id: number): Observable<Client> {
    return this.http.get<Client>(`${this.apiUrl}${id}/`);
  }

  create(client: Partial<Client>): Observable<Client> {
    return this.http.post<Client>(this.apiUrl, client);
  }

  update(id: number, client: Partial<Client>): Observable<Client> {
    return this.http.put<Client>(`${this.apiUrl}${id}/`, client);
  }

  delete(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${id}/`);
  }
}
