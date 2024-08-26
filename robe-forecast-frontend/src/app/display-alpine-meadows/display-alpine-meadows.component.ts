import { Component } from '@angular/core';
import { CommonModule } from "@angular/common";
import { RiverDataService } from '../services/river-data.services';
import { Title } from "@angular/platform-browser";

@Component({
  selector: 'app-display-alpine-meadows',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './display-alpine-meadows.component.html',
  styleUrl: './display-alpine-meadows.component.css',
  providers: [RiverDataService],
})
export class DisplayAlpineMeadowsComponent {
  alpineMeadowsData: any[] = [];

  constructor(private riverDataService: RiverDataService, private titleService: Title) {
  }

  ngOnInit(): void {
    this.getAlpineMeadowsGauge();
    this.titleService.setTitle('Robe Alpine Meadows')
  }

  getAlpineMeadowsGauge() {
    this.riverDataService.getAlpineMeadowsGauge().subscribe(data => {
      this.alpineMeadowsData = data;
    })
  }
}
