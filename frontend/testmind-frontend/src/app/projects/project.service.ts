import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Project {
  id: number;
  nome_projeto: string;
  client: { id: number; name: string };
  data_inicio: string;
  data_fim: string;
  status_projeto: string;
  status_atual: string;
}

@Injectable({
  providedIn: 'root'
})
export class ProjectService {
  private apiUrl = 'http://127.0.0.1:8000/api/projects/';

  constructor(private http: HttpClient) {}

  list(): Observable<Project[]> {
    return this.http.get<Project[]>(this.apiUrl);
  }

  get(id: number): Observable<Project> {
    return this.http.get<Project>(`${this.apiUrl}${id}/`);
  }

  create(data: Partial<Project>): Observable<Project> {
    return this.http.post<Project>(this.apiUrl, data);
  }

  update(id: number, data: Partial<Project>): Observable<Project> {
    return this.http.put<Project>(`${this.apiUrl}${id}/`, data);
  }

  delete(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}${id}/`);
  }
}
