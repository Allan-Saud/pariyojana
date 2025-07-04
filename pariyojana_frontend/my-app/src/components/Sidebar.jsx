import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => {
  const navStyle = {
    padding: '10px 20px',
    textDecoration: 'none',
    display: 'block',
    color: '#fff',
  };

  return (
    <div style={{ width: 250, background: '#2c3e50', height: '100vh', color: '#fff' }}>
      <h2 style={{ padding: 20 }}>बारदगोरिया गाउँपालिका</h2>
      <nav>
        <Link to="/" style={navStyle}>ड्यासबोर्ड</Link>
        <Link to="/projects" style={navStyle}>परियोजनाहरू</Link>
        <Link to="/auth" style={navStyle}>प्रमाणिकरण</Link>
        <Link to="/inventory" style={navStyle}>मौजुदा सुची</Link>
        <Link to="/planning" style={navStyle}>योजना तर्जुमा</Link>
        <Link to="/reports" style={navStyle}>रिपोटहरु</Link>
        <Link to="/settings" style={navStyle}>सेटिंग्स</Link>
        <Link to="/users" style={navStyle}>प्रयोगकर्ता</Link>
      </nav>
    </div>
  );
};

export default Sidebar;
