import {Component, OnInit} from '@angular/core';
import {RiverDataService} from "../services/river-data.services";

@Component({
  selector: 'app-display.records',
  standalone: true,
  imports: [],
  templateUrl: './display.records.component.html',
  styleUrl: './display.records.component.css'
})
export class DisplayRecordsComponent implements OnInit {
  riverData: any[] = [];

  constructor(private riverDataService: RiverDataService) {}

  ngOnInit(): void {
    this.riverDataService.getRiverData().subscribe(data => {
      this.riverData = data;
    })
  }

}
