import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterOutlet } from '@angular/router';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from "@angular/material/button";
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout'
import { MatIcon } from "@angular/material/icon";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, MatToolbarModule, MatButtonModule, RouterLink, MatIcon],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  isSmallScreen: boolean = false;
  isVerySmallScreen: boolean = false;
  showLinks: boolean = false;

  constructor(private breakpointObserver: BreakpointObserver) {}

  ngOnInit() {
    this.breakpointObserver.observe(Breakpoints.Handset).subscribe(result => {
      this.isSmallScreen = result.matches;
    });

    this.breakpointObserver.observe('(max-width: 450px)').subscribe(result => {
      this.isVerySmallScreen = result.matches
    });
  }

  toggleLinks() {
    this.showLinks = !this.showLinks;
  }

  title = 'robe-forecast-frontend';
}
