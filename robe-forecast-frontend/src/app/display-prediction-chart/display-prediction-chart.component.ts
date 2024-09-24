// import {Component, OnInit} from '@angular/core';
// import { CommonModule } from "@angular/common";
// import { RiverDataService } from '../services/river-data.services';
// import { Title } from "@angular/platform-browser";
//
// @Component({
//   selector: 'app-display-prediction-chart',
//   standalone: true,
//   imports: [CommonModule],
//   templateUrl: './display-prediction-chart.component.html',
//   styleUrl: './display-prediction-chart.component.css',
//   providers: [RiverDataService],  // Make sure to include the service provider
//
// })
//
// export class DisplayPredictionChartComponent implements OnInit {
//   combinedData: any[] = [];
//
//   constructor(private riverDataService: RiverDataService, private titleService: Title) {}
//
//   ngOnInit(): void {
//     this.getPredictionData();
//     this.titleService.setTitle('Robe Combined Gauges')
//   }
//
//   getPredictionData() {
//     this.riverDataService.getPredictionData().subscribe(data => {
//       this.combinedData = data;
//     });
//   }
//
// }
