import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RiverDataService {

  private baseUrl = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) {}

  getGraniteForecastChart(): Observable<any> {
    return this.http.get(`${this.baseUrl}/granitefallsforecastchart/`, { responseType: 'json' })
  }

  getGraniteForecastLinearChart(): Observable<any> {
    return this.http.get(`${this.baseUrl}/granitefallsforecastlinearchart/`, { responseType: 'json' })
  }

  getGraniteForecastTable(): Observable<any> {
    return this.http.get<any[]>(`${this.baseUrl}/granitefallsforecasttable/`)
  }

  getGraniteForecastLinearTable(): Observable<any> {
    return this.http.get<any[]>(`${this.baseUrl}/granitefallsforecastlineartable/`)
  }

  getAccuracyMetrics(): Observable <any> {
    return this.http.get<any[]>(`${this.baseUrl}/accuracymetrics/`)
  }

  getAccuracyMetricsLinear(): Observable <any> {
    return this.http.get<any[]>(`${this.baseUrl}/accuracymetricslinear/`)
  }

}

