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
  selector: 'app-box-plot',
  templateUrl: './box-plot.component.html',
  styleUrls: ['./box-plot.component.css']
})
export class BoxPlotComponent implements OnInit {
  public options: any = {
    chart: {
        type: 'boxplot'
    },

    title: {
        text: 'Box Plot'
    },

    legend: {
        enabled: false
    },

    xAxis: {
        categories: ['Maths', 'Science', 'IT', 'Music'],
        title: {
            text: 'Subjects'
        }
    },

    yAxis: {
        title: {
            text: 'Marks'
        },
        plotLines: [{
            value: 932,
            color: 'red',
            width: 1,
            label: {
                text: 'Theoretical mean: 932',
                align: 'center',
                style: {
                    color: 'gray'
                }
            }
        }]
    },

    series: [{
        name: 'Marks',
        data: [],
        tooltip: {
            headerFormat: '<em>Score {point.key}</em><br/>'
        }
    }, {
        name: 'Data',
        type: 'scatter',
        data: [],
        id: 's1',
        marker: {
            radius: 1.5
        },
        tooltip: {
            pointFormat: 'Marks: {point.y}'
        }
    }]
  }

  constructor(private service: AppDataService, private dataGet: DataPassingService) { }

  ngOnInit() {
    this.getBoxplotData('all', 'all', 2010, 10)
    Highcharts.chart('container', this.options);
  }

  
  getBoxplotData(student_id, subject_id, year, grade){
      this.service.getBoxPlotdata(student_id, subject_id, year, grade).subscribe(boxPlotData => {
        // debugger
        this.options.series[0].data[0] = boxPlotData.maths
        this.options.series[0].data[1] = boxPlotData.science
        this.options.series[0].data[2] = boxPlotData.it
        this.options.series[0].data[3] = boxPlotData.music
        // this.options.series[1].data[4] = boxPlotData.maths
        // debugger
        Highcharts.chart('container', this.options);
      })
   
  }

  generate() {
      this.dataGet.currentMessage.subscribe(msg => {
          if (msg) {
                this.getBoxplotData(msg['student_id'], msg['subject_id'], msg['year'], msg['grade'])
          }
      })
  }

}
