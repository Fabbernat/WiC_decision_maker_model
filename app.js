import React from 'react';
import Button from '@material-ui/core/Button';

const LittleApp = () => {
  return (
    <div>
      <MaterialUI.Button variant="contained" color="primary">
        Hello World
      </MaterialUI.Button>
    </div>
  )
}

ReactDOM.render(<LittleApp />, document.getElementById("littleApp"));
