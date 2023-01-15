import { Component } from '@angular/core';
import usersData from './users.json';

interface User{
  id:Number;
  name:String;
  email:String;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angular-fitness-project';

  users:User[]=usersData;
}
