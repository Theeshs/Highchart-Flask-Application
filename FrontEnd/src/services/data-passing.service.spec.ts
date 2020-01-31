import { TestBed } from '@angular/core/testing';

import { DataPassingService } from './data-passing.service';

describe('DataPassingService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: DataPassingService = TestBed.get(DataPassingService);
    expect(service).toBeTruthy();
  });
});
