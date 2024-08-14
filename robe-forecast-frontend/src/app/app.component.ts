/*import {ApplicationConfig, Component, OnInit} from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {HttpClient} from "@angular/common/http";
import {RiverDataService} from "./services/river-data.services";
import { provideHttpClient } from "@angular/common/http";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

// export const appConfig: ApplicationConfig = {
//   providers: [
//     provideHttpClient(),
//   ]
// }

export class AppComponent implements OnInit{
  title = 'robe-forecast-frontend';
  riverData: any[] = [];
  // constructor(private http: HttpClient) {}
  constructor(private riverDataService: RiverDataService) {  }

  ngOnInit(): void{
    this.riverDataService.getRiverData().subscribe(data => {
      this.riverData = data;
    })
  }
}*/
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
/*import {MatButtonModule} from "@angular/material/button";
import {MainNavComponent} from "./main-nav/main-nav.component";
import {HomeComponent} from "./home/home.component";
import {ClassroomComponent} from "./classroom/classroom.component";*/

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'paddle-whitewater';
}
