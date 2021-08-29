import React from 'react'
import './App.css';
// import './AppOld.css';
import Card from './components/Card';
import StripSmall from './components/StripSmall';
import StripLarge from './components/StripLarge';
import Navbar from './components/Navbar';
import Menu from './components/Menu';

function App() {
  return (
    <div className="mainGrid">
      <div className="menuArea" id="menuArea">
        <Menu />
      </div>
      <div className="topbarArea" id="topbarArea">
        <Navbar />
      </div>
      <div className="bodyArea" id="bodyArea">

        <div className="bodyGrid">
          <div className="leftColumn">
            <Card />
            <Card />
            <Card />
          </div>
          <div className="middleColumn">
            <Card />
            <Card />
            <Card />
          </div>
          <div className="rightColumn">
            <Card />
            <Card />
            <Card />
          </div>
        </div>

      </div>
    </div>
  );
}

export default App;
