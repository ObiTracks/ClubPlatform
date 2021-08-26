import React from 'react'
import './App.css';
// import './AppOld.css';
import Card from './components/Card';
import StripSmall from './components/StripSmall';
import StripLarge from './components/StripLarge';

function App() {
  return (
    <div className="mainGrid">
      <div className="menuArea" id="menuArea"></div>
      <div className="topbarArea" id="topbarArea"></div>
      <div className="bodyArea" id="bodyArea">

        <div className="bodyGrid">
          <div className="leftColumn"></div>
          <div className="middleColumn"></div>
          <div className="rightColumn"></div>
        </div>

      </div>
    </div>
  );
}

export default App;
