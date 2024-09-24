import { Component } from '@angular/core';
import { RiverDataService } from "../services/river-data.services";
import {DomSanitizer, Title} from "@angular/platform-browser";
import {NgForOf, NgIf} from "@angular/common";


@Component({
  selector: 'app-information',
  standalone: true,
  imports: [
    NgForOf,
    NgIf
  ],
  templateUrl: './information.component.html',
  styleUrl: './information.component.css'
})
export class InformationComponent {
  accuracyMetrics: any[] = [];
  accuracyMetricsLinear: any[] = [];

  constructor(
    private riverDataService: RiverDataService,
    private titleService: Title,
  ) {}

  ngOnInit(): void {
    this.getAccuracyMetrics();
    this.getAccuracyMetricsLinear();
    this.titleService.setTitle('Granite Forecast Info')
  }

  getAccuracyMetrics() {
    this.riverDataService.getAccuracyMetrics().subscribe( data => {
      this.accuracyMetrics = data;
    })
  }
  getAccuracyMetricsLinear() {
    this.riverDataService.getAccuracyMetricsLinear().subscribe( data => {
      this.accuracyMetricsLinear = data;
    })
  }

}
