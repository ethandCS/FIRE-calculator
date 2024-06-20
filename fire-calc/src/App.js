import React, { useState } from 'react';
import { Line } from 'react-chartjs-2';
import './App.css';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

// Register Chart.js components
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

function App() {
  const [age, setAge] = useState('');
  const [retirementAge, setRetirementAge] = useState('');
  const [salary, setSalary] = useState('');
  const [savingsRate, setSavingsRate] = useState('');
  const [investmentRate, setInvestmentRate] = useState('');
  const [chartData, setChartData] = useState({
    labels: [],
    datasets: [
      {
        label: 'Weak Investment Growth',
        data: [],
        fill: false,
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
      },
      {
        label: 'Moderate Investment Growth',
        data: [],
        fill: false,
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
      },
      {
        label: 'Strong Investment Growth',
        data: [],
        fill: false,
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
      },
    ],
  });

  const fetchData = () => {
    fetch('http://localhost:5000/calculate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        age: parseInt(age),
        retirementAge: parseInt(retirementAge),
        salary: parseFloat(salary),
        savingsRate: parseFloat(savingsRate),
        investmentRate: parseFloat(investmentRate),
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        setChartData({
          labels: data.years,
          datasets: [
            {
              ...chartData.datasets[0],
              data: data.weak,
            },
            {
              ...chartData.datasets[1],
              data: data.moderate,
            },
            {
              ...chartData.datasets[2],
              data: data.strong,
            },
          ],
        });
      });
  };

  return (
    <div className="App">
      <h1>FIRE Calculator</h1>
      <div>
        <label>
          Age:
          <input
            type="number"
            value={age}
            onChange={(e) => setAge(e.target.value)}
          />
        </label>
        <label>
          Retirement Age:
          <input
            type="number"
            value={retirementAge}
            onChange={(e) => setRetirementAge(e.target.value)}
          />
        </label>
        <label>
          Salary:
          <input
            type="number"
            value={salary}
            onChange={(e) => setSalary(e.target.value)}
          />
        </label>
        <label>
          Savings Rate (as a decimal):
          <input
            type="number"
            value={savingsRate}
            onChange={(e) => setSavingsRate(e.target.value)}
          />
        </label>
        <label>
          Investment Rate (as a decimal):
          <input
            type="number"
            value={investmentRate}
            onChange={(e) => setInvestmentRate(e.target.value)}
          />
        </label>
      </div>
      <button onClick={fetchData}>Calculate</button>
      <div className="chart-container">
        <Line data={chartData} />
      </div>
      <p>This is not official financial advice, merely a project.</p>
      <footer>
        <p>Created by Ethan Diaz</p>
      </footer>
    </div>
  );
}

export default App;
