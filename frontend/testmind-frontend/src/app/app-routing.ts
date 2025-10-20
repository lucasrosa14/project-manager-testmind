import { Routes } from '@angular/router';
import { provideRouter, withEnabledBlockingInitialNavigation } from '@angular/router';
import { ProjectListComponent } from './projects/project-list.component';
import { ProjectFormComponent } from './projects/project-form.component';
import { ProjectDetailComponent } from './projects/project-detail.components';
import { ClientListComponent } from './clients/client-list.component';
import { ClientFormComponent } from './clients/client-form.component';
import { ClientDetailComponent } from './clients/client-detail.component';
import { BugListComponent } from './bugs/bug-list.component';
import { BugFormComponent } from './bugs/bug-form.component';
import { BugDetailComponent } from './bugs/bug-detail.component';

export const routes: Routes = [
  { path: '', redirectTo: '/projects', pathMatch: 'full' },

  // Projects
  { path: 'projects', component: ProjectListComponent },
  { path: 'projects/create', component: ProjectFormComponent },
  { path: 'projects/edit/:id', component: ProjectFormComponent },
  { path: 'projects/:id', component: ProjectDetailComponent },

  // Clients
  { path: 'clients', component: ClientListComponent },
  { path: 'clients/create', component: ClientFormComponent },
  { path: 'clients/edit/:id', component: ClientFormComponent },
  { path: 'clients/:id', component: ClientDetailComponent },

  // Bugs
  { path: 'bugs', component: BugListComponent },
  { path: 'bugs/create', component: BugFormComponent },
  { path: 'bugs/edit/:id', component: BugFormComponent },
  { path: 'bugs/:id', component: BugDetailComponent },

  // Fallback
  { path: '**', redirectTo: '/projects' }
];

export const appRouter = provideRouter(routes, withEnabledBlockingInitialNavigation());
