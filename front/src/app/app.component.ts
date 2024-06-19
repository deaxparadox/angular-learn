import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';


import { BarComponent } from './d3/bar/bar.component';
import { PieComponent } from './d3/pie/pie.component';
import { ScatterComponent } from './d3/scatter/scatter.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    BarComponent,
    PieComponent,
    ScatterComponent
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'front';
}
