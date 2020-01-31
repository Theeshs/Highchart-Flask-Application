import { FormGroup, FormControl } from '@angular/forms';
import { AppDataService } from './../../services/app-data.service';
import { Component, OnInit, ViewChild } from '@angular/core';
import { BoxPlotComponent } from './box-plot/box-plot.component';
import { DataPassingService } from 'services/data-passing.service';
import { ColumnChartComponent } from './column-chart/column-chart.component';
import { OutputGraphComponent } from './output-graph/output-graph.component';
// import { format } from 'path';


declare const $: any;

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html'
})
export class DashboardComponent implements OnInit {
  students
  subjects
  years:string[] = []
  grades:number[] = []
  private error
  private filterForms = new FormGroup({
    Student: new FormControl(''),
    Subject: new FormControl(''),
    Year: new FormControl(''),
    Grade: new FormControl(''),
  })

  @ViewChild(BoxPlotComponent, {static: false}) boxPlot;
  @ViewChild(ColumnChartComponent, {static: false}) columnPlot;
  @ViewChild(OutputGraphComponent, {static: false}) progressPlot;
  constructor(private appService: AppDataService, private dataShare: DataPassingService) {}

  public ngOnInit() {
    this.appService.getFilterData().subscribe(filterData => {
      // debugger
      this.students = filterData.students
      this.subjects = filterData.subjects
      this.years = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
      this.grades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }, error => {
      this.error = error
    })
  }

  generateGraphs(form) {
    // debugger
    const details = {
      student_id: form.value.Student,
      subject_id: form.value.Subject,
      grade: form.value.Grade,
      year: form.value.Year,
    }
    this.dataShare.changeMessage(details)
    this.boxPlot.generate();
    this.columnPlot.generate();
    this.progressPlot.generate()
  }
}
