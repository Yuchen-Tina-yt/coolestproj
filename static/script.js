import { BModal, VBModal } from 'bootstrap-vue'
import React, {Component} from 'react';

 class App extends Component {
    render()
    {
      <div className="App">
        <head>
          <title>Online Audio-to-Text Converter</title>
        </head>
        <body>
          <h1>Online Audio-to-Text Converter</h1>
          <p>
            This is an online speech-to-text tool.
            It can convert your lecture recordings into text!
            Start by uploading your audio below.
          </p>
          <Button variant="contained" color="primary">
            Hello World
          </Button>
          </body>
      </div>
    }
}

React.render(
  React.createElement(App),
  document.getElementById("root")
);
