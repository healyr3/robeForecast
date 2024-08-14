import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayRecordsComponent } from './display.records.component';

describe('DisplayRecordsComponent', () => {
  let component: DisplayRecordsComponent;
  let fixture: ComponentFixture<DisplayRecordsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DisplayRecordsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DisplayRecordsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
