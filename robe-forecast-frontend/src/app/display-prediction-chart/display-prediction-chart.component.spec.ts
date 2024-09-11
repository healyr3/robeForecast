import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayPredictionChartComponent } from './display-prediction-chart.component';

describe('DisplayPredictionChartComponent', () => {
  let component: DisplayPredictionChartComponent;
  let fixture: ComponentFixture<DisplayPredictionChartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DisplayPredictionChartComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DisplayPredictionChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
