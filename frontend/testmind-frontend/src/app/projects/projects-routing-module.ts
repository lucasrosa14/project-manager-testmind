import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListComponent } from './list/list.component';
import { DetailComponent } from './detail/detail.component';
import { FormComponent } from './form.component';

const routes: Routes = [
  { path: '', component: ListComponent },
  { path: 'new', component: FormComponent },
  { path: ':id', component: DetailComponent },
  { path: ':id/edit', component: FormComponent },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProjectsRoutingModule { }
