import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [form, setForm] = useState({
    age: '',
    sex: '0',
    bmi: '',
    children: '',
    smoker: '0',
    region: '0',
  });

  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:5000/predict', {
        age: parseFloat(form.age),
        sex: parseInt(form.sex),
        bmi: parseFloat(form.bmi),
        children: parseInt(form.children),
        smoker: parseInt(form.smoker),
        region: parseInt(form.region),
      });
      setPrediction(res.data.predicted_cost.toFixed(2));
    } catch (err) {
      console.error('Error:', err);
      alert('Prediction failed. Check backend.');
    }
  };

  return (
    <div className="container">
      <h1>🧮 Medical Insurance Cost Predictor</h1>
      <form onSubmit={handleSubmit}>
        <input type="number" name="age" placeholder="Age" required onChange={handleChange} />
        <select name="sex" onChange={handleChange}>
          <option value="0">Female</option>
          <option value="1">Male</option>
        </select>
        <input type="number" step="0.1" name="bmi" placeholder="BMI" required onChange={handleChange} />
        <input type="number" name="children" placeholder="Children" required onChange={handleChange} />
        <select name="smoker" onChange={handleChange}>
          <option value="0">Non-Smoker</option>
          <option value="1">Smoker</option>
        </select>
        <select name="region" onChange={handleChange}>
          <option value="0">Southwest</option>
          <option value="1">Southeast</option>
          <option value="2">Northwest</option>
          <option value="3">Northeast</option>
        </select>
        <button type="submit">Predict</button>
      </form>
      {prediction && <h2>Predicted Cost: ₹{prediction}</h2>}
    </div>
  );
}

export default App;
