import streamlit as st
import pandas as pd
import numpy as np

st.title("🟡 Future Gold Price Prediction Analysis")

# Sample historical gold prices
prices = [1850, 1852, 1855, 1853, 1858, 1862, 1865, 1868, 1870, 1873, 1876]

df = pd.DataFrame({"Gold Price": prices})
df["Day"] = np.arange(len(df))

# Simple trend prediction
slope = (prices[-1] - prices[0]) / len(prices)

future_days = st.slider("Select future days", 5, 30, 10)

future_prices = [
    prices[-1] + slope * i for i in range(1, future_days + 1)
]

future_df = pd.DataFrame({
    "Day": range(len(df), len(df) + future_days),
    "Predicted Gold Price": future_prices
})

st.subheader("📈 Gold Price Trend")
chart_df = pd.concat([
    df.rename(columns={"Gold Price": "Price"}),
    future_df.rename(columns={"Predicted Gold Price": "Price"})
])

st.line_chart(chart_df.set_index("Day"))

st.subheader("🔮 Future Prediction Table")
st.dataframe(future_df)
