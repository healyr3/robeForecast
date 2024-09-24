import { Component, OnInit } from '@angular/core';
import { CommonModule } from "@angular/common";
import { RiverDataService } from "../services/river-data.services";
import { DomSanitizer, SafeHtml, Title } from "@angular/platform-browser";
import { PlotlyModule } from "angular-plotly.js";

@Component({
  selector: 'app-display-granite-forecast-linear',
  standalone: true,
  imports: [CommonModule, PlotlyModule],
  templateUrl: './display-granite-forecast-linear.component.html',
  styleUrl: './display-granite-forecast-linear.component.css',
  providers: [RiverDataService],
})
export class DisplayGraniteForecastLinearComponent {
  graniteLinearChartData: any;
  graniteLinearChartLayout: any;
  graniteLinearTableData: any[] = [];
  accuracyMetricsLinear: any[] = [];

  constructor(
    private riverDataService: RiverDataService,
    private titleService: Title,
    private sanitizer: DomSanitizer
  ) {}

  ngOnInit(): void {
    this.getGraniteForecastLinearChart();
    this.getGraniteForecastLinearTable();
    this.getAccuracyMetricsLinear();
    this.titleService.setTitle('Granite Forecast Linear Chart')
  }

  getGraniteForecastLinearChart() {
    this.riverDataService.getGraniteForecastLinearChart().subscribe(data => {
      if (data.chart) {
        this.graniteLinearChartData = data.chart.data;
        this.graniteLinearChartLayout = data.chart.layout;
        console.log('Chart data: ', this.graniteLinearChartData);
        console.log('Chart layout: ', this.graniteLinearChartLayout);
      } else {
        console.error('Chart data not found')
      }
    })
  }

  getGraniteForecastLinearTable() {
    this.riverDataService.getGraniteForecastLinearTable().subscribe(data => {
      this.graniteLinearTableData = data;
    });
  }

  getAccuracyMetricsLinear() {
    this.riverDataService.getAccuracyMetricsLinear().subscribe( data => {
      this.accuracyMetricsLinear = data;
    })
  }

}
