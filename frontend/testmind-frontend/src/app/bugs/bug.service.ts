import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Bug {
  id: number;
  title: string;
  description?: string;
  project: number; // project ID
  status: string;
}

@Injectable({
  providedIn: 'root'
})
export class BugService {
  private apiUrl = '/api/bugs/';

  constructor(private http: HttpClient) {}

  list(): Observable<Bug[]> {
    return this.http.get<Bug[]>(this.apiUrl);
  }

  get(id: number): Observable<Bug> {
    return this.http.get<Bug>(`${this.apiUrl}${id}/`);
  }

  create(bug: Partial<Bug>): Observable<Bug> {
    return this.http.post<Bug>(this.apiUrl, bug);
  }

  update(id: number, bug: Partial<Bug>): Observable<Bug> {
    return this.http.put<Bug>(`${this.apiUrl}${id}/`, bug);
  }

  delete(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${id}/`);
  }
}
