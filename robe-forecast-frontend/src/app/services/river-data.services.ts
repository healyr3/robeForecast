import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RiverDataService {

  private baseUrl = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) {}

  getGraniteFallsData(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/granitefalls/`);
  }

  getJordanRoadData(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/jordanroad/`);
  }

  getVerlotData(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/verlot/`);
  }

  getCombinedData(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/combinedgauges/`)
  }

  getSilvertonWeatherPrediction(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/silvertonprediction/`)
  }

  getAlpineMeadowsGauge(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/alpinemeadows/`)
  }

  getJordanChart(): Observable<any> {
    return this.http.get(`${this.baseUrl}/jordanchart/`, { responseType: 'json' })
  }

}

