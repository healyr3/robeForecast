// import { Component, OnInit } from '@angular/core';
// import { RiverDataService } from '../services/river-data.services';
// import { CommonModule } from "@angular/common";
// import { Title } from "@angular/platform-browser";
//
// @Component({
//   selector: 'app-display-records',
//   standalone: true,
//   templateUrl: './display.records.component.html',
//   styleUrls: ['./display.records.component.css'],
//   providers: [RiverDataService],  // Make sure to include the service provider
//   imports: [CommonModule]
// })
// export class DisplayRecordsComponent implements OnInit {
//   graniteFallsData: any[] = [];
//   jordanRoadData: any[] = [];
//
//   constructor(private riverDataService: RiverDataService, private titleService: Title) {}
//
//   ngOnInit(): void {
//     this.getRiverData();
//     this.titleService.setTitle('Robe Display Rivers')
//   }
//
//   getRiverData() {
//     this.riverDataService.getGraniteFallsData().subscribe(data => {
//       this.graniteFallsData = data;
//     });
//
//     this.riverDataService.getJordanRoadData().subscribe(data => {
//       this.jordanRoadData = data;
//     });
//   }
// }
