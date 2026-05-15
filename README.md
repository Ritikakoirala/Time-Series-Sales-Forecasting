📈 Sales Time Series Forecasting using ARIMA & Streamlit
Project Overview

This project focuses on forecasting future sales using historical sales data. It uses time series analysis techniques and builds an interactive web application using Streamlit.

The core forecasting model used is Autoregressive Integrated Moving Average (ARIMA), which is widely used for predicting future values based on past trends.
🎯 Objective
Analyze historical sales data
Identify trends and patterns over time
Build a forecasting model using ARIMA
Deploy an interactive web app using Streamlit
Predict future sales values
📊 Dataset Information

The dataset contains retail sales transactions with features such as:
Order Date
Sales
Category
Region
Product details
For forecasting, only Order Date and Sales are used after preprocessing.

🧹 Data Preprocessing Steps
Converted Order Date to datetime format
Removed irrelevant columns
Aggregated sales by date
Handled missing values using forward fill
Resampled data to daily frequency
🧠 Model Used

The forecasting model used is:

📌 ARIMA (AutoRegressive Integrated Moving Average)

ARIMA is a statistical model used for time series forecasting that captures:

Autocorrelation
Trend
Noise

It is represented as ARIMA(p, d, q).

🛠️ Technologies Used
Python 🐍
Pandas 📊
Matplotlib 📉
Statsmodels 📦
Streamlit 🌐
Scikit-learn 🤖
🚀 Features of the Web App
Upload CSV dataset
View actual sales trends
Generate future sales forecasts
Adjustable forecast horizon (7–60 days)
Interactive charts
