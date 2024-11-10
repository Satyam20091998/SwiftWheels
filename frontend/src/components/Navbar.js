// D:\SwiftWheels\SwiftWheels\frontend\src\components\Navbar.js

import React from 'react';
import { Link } from 'react-router-dom'; // Import Link

export function Navbar() {
  return (
    <div className="navbar">
      <div className="logo">SwiftWheels</div>
      <div className="menu">
        <button>Login</button>
        {/* Use Link here for navigation */}
        <Link to="/register">
          <button>Sign Up</button>
        </Link>
      </div>
    </div>
  );
}
