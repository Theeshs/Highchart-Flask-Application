import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { API_URL } from 'app/env';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AppDataService {

  constructor(private http: HttpClient) { }

  getFilterData(): Observable<any> {
    return this.http.get(`${API_URL}/get-filter-data`)
  }

  getBoxPlotdata(student_id, subject_id, year, grade): Observable<any> {
    return this.http.get(`${API_URL}/get-marks`, {params: {student_id: student_id, subject_id: subject_id, year: year, grade: grade}})
  }

  getColumnPlotData(student_id, subject_id, year, grade): Observable<any> {
    return this.http.get(`${API_URL}/get-marks-column`, {params: {student_id: student_id, subject_id: subject_id, year: year, grade: grade}})
  }

  getSemester1Data(student_id): Observable<any> {
    return this.http.get(`${API_URL}/all_sub_student_sem_1`,{params: {student_id: student_id}})
  }

  getSemester2Data(student_id): Observable<any> {
    return this.http.get(`${API_URL}/all_sub_student_sem_2`,{params: {student_id: student_id}})
  }
}
