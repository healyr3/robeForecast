import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplaySilvertonPredictionComponent } from './display-silverton-prediction.component';

describe('DisplaySilvertonPredictionComponent', () => {
  let component: DisplaySilvertonPredictionComponent;
  let fixture: ComponentFixture<DisplaySilvertonPredictionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DisplaySilvertonPredictionComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DisplaySilvertonPredictionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
