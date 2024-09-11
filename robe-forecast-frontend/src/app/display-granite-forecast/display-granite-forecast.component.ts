import { Component, OnInit } from '@angular/core';
import { CommonModule } from "@angular/common";
import { RiverDataService } from "../services/river-data.services";
import { DomSanitizer, SafeHtml, Title } from "@angular/platform-browser";
import {PlotlyModule} from "angular-plotly.js";
@Component({
  selector: 'app-display-granite-forecast',
  standalone: true,
  imports: [CommonModule, PlotlyModule],
  templateUrl: './display-granite-forecast.component.html',
  styleUrl: './display-granite-forecast.component.css',
  providers: [RiverDataService],
})
export class DisplayGraniteForecastComponent implements OnInit {
  graniteChartData: any;
  graniteChartLayout: any;
  graniteTableData: any[] = [];

  constructor(
    private riverDataService: RiverDataService,
    private titleService: Title,
    private sanitizer: DomSanitizer
  ) {}

  ngOnInit(): void {
    this.getGraniteForecastChart();
    this.getGraniteForecastTable();
    this.titleService.setTitle('Granite Forecast Chart')
  }

  getGraniteForecastChart() {
    this.riverDataService.getGraniteForecastChart().subscribe(data => {
      if (data.chart) {
        this.graniteChartData = data.chart.data;
        this.graniteChartLayout = data.chart.layout;
        console.log('Chart data: ', this.graniteChartData);
        console.log('Chart layout: ', this.graniteChartLayout);
      } else {
        console.error('Chart data not found')
      }
    })
  }

  getGraniteForecastTable() {
    this.riverDataService.getGraniteForecastTable().subscribe(data => {
      this.graniteTableData = data;
    });
  }
}
