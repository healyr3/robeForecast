import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayGraniteForecastLinearComponent } from './display-granite-forecast-linear.component';

describe('DisplayGraniteForecastLinearComponent', () => {
  let component: DisplayGraniteForecastLinearComponent;
  let fixture: ComponentFixture<DisplayGraniteForecastLinearComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DisplayGraniteForecastLinearComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DisplayGraniteForecastLinearComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
