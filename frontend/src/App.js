import React, { useState } from 'react'
import axios from 'axios';

function App() {
  const [input_city, setCity] = useState("");
  const [weather, setWeather] = useState(null);

  const fetchWeather = async (input_city) => {
    console.log("123");
    try {
      const response = await axios.post('http://localhost:3000/weather', { city: "Лондон"});
      console.log(response.data);
    } catch (error) {
      console.error('Error fetching weather data', error);
    }
  };

  return (
    <div className="App">
  <h1>Прогноз погоды</h1>
  <input
    type="text"
    value={input_city}
    onChange={(e) => setCity(e.target.value)}
    placeholder="Введите город" 
  />
  <button onClick={() => fetchWeather()}>Get weather</button>
  {weather && (
    <div className="weather-info"> 
      <h2>{weather.city}</h2>
      <p>Temperature: {weather.temperature} C</p>
      <p>Description: {weather.description}</p>
    </div>
  )}
</div>
  )
};


export default App;