import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideHttpClient } from '@angular/common/http';
import { provideRouter } from '@angular/router';
import { routes } from './app/app.routes';
import { CommonModule } from "@angular/common";

import * as PlotlyJS from 'plotly.js-dist-min'
// import * as PlotlyJS from 'plotly.js'
import { PlotlyModule } from "angular-plotly.js";
import {NgModule} from "@angular/core";

PlotlyModule.plotlyjs = PlotlyJS

@NgModule({
  // imports: [CommonModule, PlotlyModule]
  imports: [CommonModule, PlotlyModule]
})
export class Main { }

bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient(),
    provideRouter(routes),
  ]
}).catch((err) => console.error(err));

