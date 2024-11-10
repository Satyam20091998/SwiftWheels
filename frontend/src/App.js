// D:\SwiftWheels\SwiftWheels\frontend\src\App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Navbar } from './components/Navbar';
import { RideOptions } from './components/RideOptions';
import { MapView } from './components/MapView';
import { Registration } from './pages/Registration'; // Ensure this is correctly imported

function App() {
  return (
    <Router>
      <div className="app">
        <Navbar />

        <div className="content">
          <Routes>
            {/* Home page */}
            <Route path="/" element={<><MapView /><RideOptions /></>} />
            
            {/* Registration page */}
            <Route path="/register" element={<Registration />} /> {/* Make sure this is present */}
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
