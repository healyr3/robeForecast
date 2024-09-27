import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayCombinedGaugesComponent } from './display-combined-gauges.component';

describe('DisplayCombinedGaugesComponent', () => {
  let component: DisplayCombinedGaugesComponent;
  let fixture: ComponentFixture<DisplayCombinedGaugesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DisplayCombinedGaugesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DisplayCombinedGaugesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
