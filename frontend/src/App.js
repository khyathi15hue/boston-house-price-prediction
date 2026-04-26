import React, { useState } from "react";
import "./App.css";

function App() {

  const [formData, setFormData] = useState({
    CRIM: "",
    ZN: "",
    INDUS: "",
    CHAS: "",
    NOX: "",
    RM: "",
    AGE: "",
    DIS: "",
    RAD: "",
    TAX: "",
    PTRATIO: "",
    B: "",
    LSTAT: ""
  });

  const [prediction, setPrediction] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
      });

      const data = await response.json(); // parse as JSON
      setPrediction(data.prediction); // use the 'prediction' key
    } catch (error) {
      console.error("Error fetching prediction:", error);
      setPrediction("Error! Could not fetch prediction.");
    }
  };

  return (
    <div className="container">
      <h1>🏠 House Price Predictor</h1>

      <form onSubmit={handleSubmit}>
        {Object.keys(formData).map((key) => (
          <input
            key={key}
            type="number"
            name={key}
            placeholder={key}
            step="any"
            onChange={handleChange}
            required
          />
        ))}

        <button type="submit">Predict Price</button>
      </form>

      {prediction && <h2>Estimated Price: ${prediction}</h2>}
    </div>
  );
}

export default App;