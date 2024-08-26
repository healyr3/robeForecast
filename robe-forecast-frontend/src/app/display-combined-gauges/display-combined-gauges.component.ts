import {Component, OnInit} from '@angular/core';
import { CommonModule } from "@angular/common";
import { RiverDataService } from '../services/river-data.services';
import { Title } from "@angular/platform-browser";

@Component({
  selector: 'app-display-combined-gauges',
  standalone: true,
  templateUrl: './display-combined-gauges.component.html',
  styleUrl: './display-combined-gauges.component.css',
  providers: [RiverDataService],  // Make sure to include the service provider
  imports: [CommonModule],
})

export class DisplayCombinedGaugesComponent implements OnInit {
  combinedData: any[] = [];

  constructor(private riverDataService: RiverDataService, private titleService: Title) {}

  ngOnInit(): void {
    this.getRiverData();
    this.titleService.setTitle('Robe Combined Gauges')
  }

  getRiverData() {
    this.riverDataService.getCombinedData().subscribe(data => {
      this.combinedData = data;
    });
  }

}
