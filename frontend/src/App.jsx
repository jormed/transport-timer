import { useState, useEffect } from 'react';

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch('/api/hello')
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => console.error("Something is wrong, Error trying to conect with backend", error));
  }, []);

  return (
    <>
      <div>
        <h1>Message from backend:</h1>
        <p>{message}</p>
      </div>
    </>
  )
}

export default App;
