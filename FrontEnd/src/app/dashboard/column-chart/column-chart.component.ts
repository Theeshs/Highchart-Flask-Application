import { AppDataService } from './../../../services/app-data.service';
import { Component, OnInit } from '@angular/core';

import * as Highcharts from 'highcharts';
import { DataPassingService } from 'services/data-passing.service';

declare var require: any;
let Boost = require('highcharts/modules/boost');
let noData = require('highcharts/modules/no-data-to-display');
let More = require('highcharts/highcharts-more');

Boost(Highcharts);
noData(Highcharts);
More(Highcharts);
noData(Highcharts);


@Component({
  selector: 'app-column-chart',
  templateUrl: './column-chart.component.html',
  styleUrls: ['./column-chart.component.css']
})
export class ColumnChartComponent implements OnInit {
  public options: any = {
    chart: {
        zoomType: 'xy'
    },
    title: {
        text: 'Marks of Students'
    },
    subtitle: {
        text: 'Average Marks vs Marks'
    },
    xAxis: [{
        categories: ["Maths", "Science", "IT", "Music"],
        crosshair: true
    }],
    yAxis: [{ // Primary yAxis
        labels: {
            format: '{value}',
            style: {
                color: Highcharts.getOptions().colors[1]
            }
        },
        title: {
            text: 'Marks',
            style: {
                color: Highcharts.getOptions().colors[1]
            }
        }
    }, { // Secondary yAxis
        title: {
            text: 'Marks',
            style: {
                color: Highcharts.getOptions().colors[0]
            }
        },
        labels: {
            format: '',
            style: {
                color: Highcharts.getOptions().colors[0]
            }
        },
        opposite: true
    }],
    tooltip: {
        shared: true
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        x: 120,
        verticalAlign: 'top',
        y: 100,
        floating: true,
        backgroundColor:
            Highcharts.defaultOptions.legend.backgroundColor || // theme
            'rgba(255,255,255,0.25)'
    },
    series: [{
        name: 'Marks',
        type: 'column',
        yAxis: 1,
        data: [],
        tooltip: {
            valueSuffix: ''
        }

    }, {
        name: 'Average',
        type: 'spline',
        data: [],
        tooltip: {
            valueSuffix: ''
        }
    }]
  }

  constructor(private service: AppDataService, private dataGet: DataPassingService) { }

  ngOnInit() {
    // debugger
    this.getColumnPlotData('all', 'all', 2010, 10)
    Highcharts.chart('container2', this.options);
  }

  getColumnPlotData(student_id, subject_id, year, grade) {
    this.service.getColumnPlotData(student_id, subject_id, year, grade).subscribe(columnPlotData => {
        debugger
        this.options.series[0].data = columnPlotData.data
        this.options.series[1].data = columnPlotData.average
        // debugger
        Highcharts.chart('container2', this.options);
    }, err => {
        debugger
    })
  }

  generate() {
      debugger
    this.dataGet.currentMessage.subscribe(msg => {
        debugger
        if (msg) {
            this.getColumnPlotData(msg['student_id'], msg['subject_id'], msg['year'], msg['grade'])
        }
    })
  }



}
