import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayJordanChartComponent } from './display-jordan-chart.component';

describe('DisplayJordanChartComponent', () => {
  let component: DisplayJordanChartComponent;
  let fixture: ComponentFixture<DisplayJordanChartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DisplayJordanChartComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DisplayJordanChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
