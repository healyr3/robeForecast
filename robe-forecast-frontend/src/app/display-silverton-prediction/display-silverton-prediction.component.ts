import { Component, OnInit } from '@angular/core';
import { CommonModule } from "@angular/common";
import { RiverDataService } from '../services/river-data.services';
import { Title } from "@angular/platform-browser";

@Component({
  selector: 'app-display-silverton-prediction',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './display-silverton-prediction.component.html',
  styleUrl: './display-silverton-prediction.component.css',
  providers: [RiverDataService],  // Make sure to include the service provider

})
export class DisplaySilvertonPredictionComponent {
  silvertonData: any[] = [];

  constructor(private riverDataService: RiverDataService, private titleService: Title) {
  }

  ngOnInit(): void {
    this.getSilvertonWeatherPrediction();
    this.titleService.setTitle('Robe Silverton Forecast')
  }

  getSilvertonWeatherPrediction() {
    this.riverDataService.getSilvertonWeatherPrediction().subscribe(data => {
      this.silvertonData = data;
    })
  }
}
