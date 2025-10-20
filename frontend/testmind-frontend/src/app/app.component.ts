// app.component.ts
import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    MatSidenavModule,
    MatToolbarModule,
    MatListModule,
    MatIconModule,
    BrowserAnimationsModule
  ],
  template: `
    <mat-sidenav-container class="sidenav-container" autosize>
      <mat-sidenav mode="side" opened class="sidenav">
        <mat-toolbar color="primary">TestMind</mat-toolbar>
        <mat-nav-list>
          <a mat-list-item routerLink="/projects" routerLinkActive="active">
            <mat-icon>folder</mat-icon>
            <span>Projects</span>
          </a>
          <a mat-list-item routerLink="/clients" routerLinkActive="active">
            <mat-icon>people</mat-icon>
            <span>Clients</span>
          </a>
          <a mat-list-item routerLink="/bugs" routerLinkActive="active">
            <mat-icon>bug_report</mat-icon>
            <span>Bugs</span>
          </a>
        </mat-nav-list>
      </mat-sidenav>

      <mat-sidenav-content class="sidenav-content">
        <mat-toolbar color="primary">
          <span>Dashboard</span>
        </mat-toolbar>
        <div class="content">
          <router-outlet></router-outlet>
        </div>
      </mat-sidenav-content>
    </mat-sidenav-container>
  `,
  styles: [`
    .sidenav-container {
      height: 100vh;
    }
    .sidenav {
      width: 250px;
    }
    .sidenav-content .content {
      padding: 16px;
    }
    .mat-toolbar.mat-primary {
      color: white;
    }
    a.active {
      font-weight: bold;
      color: #1976d2;
    }
  `]
})
export class AppComponent {}
