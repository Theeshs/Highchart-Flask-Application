import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import {
  AgmCoreModule
} from '@agm/core';
import { DashboardComponent } from './dashboard.component';

import { DashboardRoutes } from './dashboard.routing';
import { OutputGraphComponent } from './output-graph/output-graph.component';
import { BoxPlotComponent } from './box-plot/box-plot.component';
import { ColumnChartComponent } from './column-chart/column-chart.component';

@NgModule({
    imports: [
        CommonModule,
        RouterModule.forChild(DashboardRoutes),
        FormsModule,
        ReactiveFormsModule,
        AgmCoreModule.forRoot({
          apiKey: 'YOUR_GOOGLE_MAPS_API_KEY'
        })
    ],
    declarations: [DashboardComponent, OutputGraphComponent, BoxPlotComponent, ColumnChartComponent],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})

export class DashboardModule {}
