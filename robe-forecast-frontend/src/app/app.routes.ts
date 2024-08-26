import { Routes } from '@angular/router';
import { LandingPageComponent } from "./landing.page/landing.page.component";
import { DisplayRecordsComponent } from "./display.records/display.records.component";
import { DisplayCombinedGaugesComponent } from "./display-combined-gauges/display-combined-gauges.component";
import {
  DisplaySilvertonPredictionComponent
} from "./display-silverton-prediction/display-silverton-prediction.component";
import {DisplayAlpineMeadowsComponent} from "./display-alpine-meadows/display-alpine-meadows.component";
import {DisplayJordanChartComponent} from "./display-jordan-chart/display-jordan-chart.component";

export const routes: Routes = [
  { path: '', component: LandingPageComponent },
  { path: 'display-records', component: DisplayRecordsComponent },
  { path: 'display-combined-gauges', component: DisplayCombinedGaugesComponent },
  { path: 'display-silverton-prediction', component: DisplaySilvertonPredictionComponent },
  { path: 'display-alpine-meadows', component: DisplayAlpineMeadowsComponent },
  { path: 'display-jordan-chart', component: DisplayJordanChartComponent },
];
