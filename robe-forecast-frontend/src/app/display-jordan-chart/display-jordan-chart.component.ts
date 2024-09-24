// import { Component, OnInit } from '@angular/core';
// import { CommonModule } from "@angular/common";
// import { RiverDataService } from "../services/river-data.services";
// import { DomSanitizer, SafeHtml, Title } from "@angular/platform-browser";
// import {PlotlyModule} from "angular-plotly.js";
//
// @Component({
//   selector: 'app-display-jordan-chart',
//   standalone: true,
//   imports: [CommonModule, PlotlyModule],
//   templateUrl: './display-jordan-chart.component.html',
//   styleUrl: './display-jordan-chart.component.css',
//   providers: [RiverDataService],
// })
// export class DisplayJordanChartComponent implements OnInit {
//    // jordanChart: SafeHtml = '';
//   jordanChartData: any;
//   jordanChartLayout: any;
//
//   constructor(
//     private riverDataService: RiverDataService,
//     private titleService: Title,
//     private sanitizer: DomSanitizer
//   ) {}
//
//   ngOnInit(): void {
//     this.getJordanChart();
//     this.titleService.setTitle('Robe Jordan Chart')
//   }
//
//   getJordanChart() {
//     this.riverDataService.getJordanChart().subscribe(data => {
//       // console.log(data);
//       // if (data.chart) {
//       //   console.log('Chart HTML:', data.chart); // Confirming chart data presence
//       // } else {
//       //   console.log('Chart data not found');
//       // }
//       if (data.chart) {
//         this.jordanChartData = data.chart.data;
//         this.jordanChartLayout = data.chart.layout;
//         console.log('Chart data: ', this.jordanChartData);
//         console.log('Chart layout: ', this.jordanChartLayout);
//       } else {
//         console.error('Chart data not found')
//       }
//       // this.jordanChart = this.sanitizer.bypassSecurityTrustHtml(data.chart);
//     })
//   }
// }
