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
  selector: 'app-output-graph',
  templateUrl: './output-graph.component.html',
  styleUrls: ['./output-graph.component.css']
})
export class OutputGraphComponent implements OnInit {
  id = 1
  public options: any = {
    title: {
        text: 'Growth by Subjects, 2010-2020'
    },

    subtitle: {
        text: 'Semester 1'
    },

    yAxis: {
        title: {
            text: 'Mark'
        }
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 2010
        }
    },

    series: [{
        name: 'Maths',
        data: []
    }, {
        name: 'Science',
        data: []
    }, {
        name: 'IT',
        data: []
    }, {
        name: 'Music',
        data: []
    }],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
  }

  public options2: any = {
    title: {
        text: 'Growth by Subjects, 2010-2020'
    },

    subtitle: {
        text: 'Semester 2'
    },

    yAxis: {
        title: {
            text: 'Mark'
        }
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 2010
        }
    },

    series: [{
        name: 'Maths',
        data: []
    }, {
        name: 'Science',
        data: []
    }, {
        name: 'IT',
        data: []
    }, {
        name: 'Music',
        data: []
    }],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
  }

  constructor(private appDataService: AppDataService, private datapass: DataPassingService) { }

  ngOnInit(){
    this.getSem1Data(this.id)
    this.getSem2Data(this.id)
    
    Highcharts.chart('container3', this.options);
    Highcharts.chart('container4', this.options2);
  }

  getSem1Data(student_id) {
      this.appDataService.getSemester1Data(student_id).subscribe(sem1 => {
        //   debugger
        this.options.series[0].data = sem1.maths
        this.options.series[1].data = sem1.science
        this.options.series[2].data = sem1.it
        this.options.series[3].data = sem1.music
        Highcharts.chart('container3', this.options);
      }, error => {
          debugger
      })
  }

  getSem2Data(student_id) {
    this.appDataService.getSemester2Data(student_id).subscribe(sem2 => {
        // debugger
      this.options2.series[0].data = sem2.maths
      this.options2.series[1].data = sem2.science
      this.options2.series[2].data = sem2.it
      this.options2.series[3].data = sem2.music
      Highcharts.chart('container4', this.options2);
    }, error => {
        debugger
    })
}

generate(){
    this.datapass.currentMessage.subscribe(msg => {
        if (msg['student_id'] != this.id) {
            this.options.series[0].data = []
            this.options.series[1].data = []
            this.options.series[2].data = []
            this.options.series[3].data = []
            this.options2.series[0].data = []
            this.options2.series[1].data = []
            this.options2.series[2].data = []
            this.options2.series[3].data = []
            Highcharts.chart('container3', this.options2);
            Highcharts.chart('container4', this.options2);
            this.getSem1Data(msg['student_id'])
            this.getSem2Data(msg['student_id'])
            this.id = msg['student_id']
        }
    })
}


}