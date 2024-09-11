import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayGraniteForecastComponent } from './display-granite-forecast.component';

describe('DisplayGraniteForecastComponent', () => {
  let component: DisplayGraniteForecastComponent;
  let fixture: ComponentFixture<DisplayGraniteForecastComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DisplayGraniteForecastComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DisplayGraniteForecastComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
