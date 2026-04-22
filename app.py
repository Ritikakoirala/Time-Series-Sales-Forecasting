import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

st.title("📈 Sales Forecasting using ARIMA")

# Upload file
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

    # Prepare data
    daily_sales = df.groupby('Order Date')['Sales'].sum()
    daily_sales = daily_sales.sort_index()
    daily_sales = daily_sales.asfreq('D')
    daily_sales = daily_sales.ffill()

    st.subheader("📊 Actual Sales Data")
    st.line_chart(daily_sales)

    # ARIMA model
    model = ARIMA(daily_sales, order=(5,1,0))
    model_fit = model.fit()

    steps = st.slider("Forecast Days", 7, 60, 30)

    forecast = model_fit.forecast(steps=steps)

    st.subheader("🔮 Forecasted Sales")
    st.line_chart(forecast)

    # Plot combined
    fig, ax = plt.subplots()
    ax.plot(daily_sales, label="Actual")
    ax.plot(forecast, label="Forecast", color="red")
    ax.legend()
    st.pyplot(fig)