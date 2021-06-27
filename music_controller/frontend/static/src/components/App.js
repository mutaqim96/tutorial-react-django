import React, { Component } from "react";
import { render } from "react-dom";


// cara nak setup class dalam react
export default class App extends{

  constructor(props){
    super(props);
  }

  render(){
    return <h1>Testing React Code</h1>
}
}

//target dulu divnya
const appDiv = document.getElementById('app');
//render the app component inside the app div
render(<App />, appDiv)