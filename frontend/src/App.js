import React, { useState } from React
import axios from "axios"

function App() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);

  const fetchWeather = async () => {
    try {
      const response = await axios.post("/weather", {city});
      setWeather(response.data);
    } catch {
      console.error("Error fetching weather data", error);
      setWeather(null);
    }
  }

  return (
    <div classname = "App">
      <h1>Прогноз погоды</h1>
      <input
        type = "text"
        value = {city}
        onChange = {(e) => setCity(e.target.value)}
        placeholder = "Введите город" 
      />
      <button onClick = {fetchWeather}>Get weather</button>
      {weather && (
        <div> 
          <h2>{weather.city}</h2>
          <p>Temperature: {weather.temperature} C</p>
          <p>Description: {weather.description}</p>
        </div>
      )}
    </div>
  )
};


export default App;