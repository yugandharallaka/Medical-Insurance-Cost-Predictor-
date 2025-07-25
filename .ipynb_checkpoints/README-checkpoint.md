
<h1 align="center">🏥 Medical Insurance Cost Predictor</h1>

<div align="center">
  <h4>Accurately predict the insurance cost of an individual using a Machine Learning model trained on demographic and health-related features.</h4><br>
  <img src="https://www.tastefulspace.com/wp-content/uploads/2023/07/187809-medical-insurance-1.webp" alt="demo" width="500"/>
</div>

---

## 😇 Motivation

Medical insurance pricing has always been a black box for most people. I was curious about how companies calculate the premium cost, so I decided to dig deep with data! With this project, I aimed to predict insurance charges based on user-specific features like age, BMI, region, and more.

---

## 📸 Some Screenshots

<p align="center">
  <img src="https://github.com/YugandharAllaka/medical-insurance-cost-predictor/blob/main/assets/correlation.png" width="400"/>
  <img src="https://github.com/YugandharAllaka/medical-insurance-cost-predictor/blob/main/assets/age_vs_charges.png" width="400"/>
  <img src="https://github.com/YugandharAllaka/medical-insurance-cost-predictor/blob/main/assets/deployment.png" width="400"/>
</p>

---

## ⭐ Features

- 🧾 Dataset Exploration
- 🔄 Encoding Categorical Variables
- 🌡️ Heatmap Analysis to identify influential features
- 📊 Data Visualization (Histograms, Boxplots, Pairplots)
- 📈 Skewness and Kurtosis Plotting
- 🧹 Data Cleaning and Preparation
- 🤖 Model Training with:
  - Linear Regression
  - SVR (Support Vector Regressor)
  - Ridge Regression
  - Random Forest Regressor (Best Model)
- 🛠️ Hyperparameter Tuning using GridSearchCV
- 📉 Model Comparison using RMSE & R² Score
- 🌐 Backend Deployment using Flask
- 🚀 Frontend Deployment using Streamlit

---

## 🔑 Results

- Achieved **R² Score of 0.87** on the test data using **Random Forest Regressor**
- Predicted medical insurance cost with high accuracy based on user input

---

## 📁 Dataset

The dataset used in this project is publicly available on Kaggle:  
👉 [Click here to download](https://www.kaggle.com/mirichoi0218/insurance)

---

## ⚙️ Installation and Running Instructions

### 1. Install dependencies:
```bash
pip install -r requirements.txt
