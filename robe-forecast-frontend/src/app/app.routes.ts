import { Routes } from '@angular/router';
import { DisplayGraniteForecastComponent } from "./display-granite-forecast/display-granite-forecast.component";
import { DisplayGraniteForecastLinearComponent } from "./display-granite-forecast-linear/display-granite-forecast-linear.component";
import { InformationComponent } from "./information/information.component";

export const routes: Routes = [
  { path: '', component: DisplayGraniteForecastComponent },
  { path: 'display-granite-forecast', component: DisplayGraniteForecastComponent },
  { path: 'display-granite-forecast-linear', component: DisplayGraniteForecastLinearComponent },
  { path: 'information', component: InformationComponent}

];
