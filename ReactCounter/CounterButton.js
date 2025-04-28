import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';

function Counter() {
  const [count, setCount] = useState(0);
  const handleClick = () => {
    setCount(prev => prev + 1);
  }

  return (
    <div id="mainArea">
      <p>button count: <span>{count}</span></p>
      <button 
        id="mainButton" 
        onClick={handleClick}
      >
        increase
      </button>
    </div>
  );
}

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<Counter />);