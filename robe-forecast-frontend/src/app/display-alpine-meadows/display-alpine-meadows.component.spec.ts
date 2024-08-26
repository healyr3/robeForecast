import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayAlpineMeadowsComponent } from './display-alpine-meadows.component';

describe('DisplayAlpineMeadowsComponent', () => {
  let component: DisplayAlpineMeadowsComponent;
  let fixture: ComponentFixture<DisplayAlpineMeadowsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DisplayAlpineMeadowsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DisplayAlpineMeadowsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
