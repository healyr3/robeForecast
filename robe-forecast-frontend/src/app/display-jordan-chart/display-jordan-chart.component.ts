import { Component, OnInit } from '@angular/core';
import { CommonModule } from "@angular/common";
import { RiverDataService } from "../services/river-data.services";
import {DomSanitizer, SafeHtml, Title} from "@angular/platform-browser";

@Component({
  selector: 'app-display-jordan-chart',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './display-jordan-chart.component.html',
  styleUrl: './display-jordan-chart.component.css',
  providers: [RiverDataService],
})
export class DisplayJordanChartComponent implements OnInit {
   jordanChart: SafeHtml = '';

  constructor(private riverDataService: RiverDataService, private titleService: Title, private sanitizer: DomSanitizer) {
  }

  ngOnInit(): void {
    this.getJordanChart();
    // this.jordanChart = this.sanitizer.bypassSecurityTrustHtml('<div>Chart HTML Here</div>');
    this.titleService.setTitle('Robe Jordan Chart')
  }

  getJordanChart() {
    this.riverDataService.getJordanChart().subscribe(data => {
      this.jordanChart = this.sanitizer.bypassSecurityTrustHtml(data.chart);
    })
  }
}
