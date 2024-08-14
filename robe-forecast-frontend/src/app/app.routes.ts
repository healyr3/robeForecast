import { Routes } from '@angular/router';
import {LandingPageComponent} from "./landing.page/landing.page.component";
import { DisplayRecordsComponent } from "./display.records/display.records.component";

export const routes: Routes = [
  { path: '', component: LandingPageComponent },
  { path: 'displayrecords', component: DisplayRecordsComponent }
];
