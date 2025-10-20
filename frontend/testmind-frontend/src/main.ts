import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter } from '@angular/router';
import { provideForms } from '@angular/forms';
import { AppComponent } from './app/app.component';
import { routes } from './app/app-routing';

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),
    provideForms()
  ]
});
