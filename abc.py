import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Future Gold Price Prediction", page_icon="🟡")

st.title("🟡 Future Gold Price Prediction Analysis")
st.markdown("Offline trend-based gold price forecasting")

# Sample historical gold price data
prices = [
    1850, 1852, 1855, 1853, 1858, 1862,
    1865, 1868, 1870, 1873, 1876
]

df = pd.DataFrame({"Price": prices})
df["Day"] = np.arange(len(df))

# Simple trend calculation
slope = (df["Price"].iloc[-1] - df["Price"].iloc[0]) / len(df)

future_days = st.slider("Select future days to predict", 5, 30, 10)

future_prices = [
    df["Price"].iloc[-1] + slope * i for i in range(1, future_days + 1)
]

future_df = pd.DataFrame({
    "Day": range(len(df), len(df) + future_days),
    "Predicted Gold Price": future_prices
})

# Plot
fig, ax = plt.subplots()
ax.plot(df["Day"], df["Price"], label="Historical Price")
ax.plot(future_df["Day"], future_df["Predicted Gold Price"],
        linestyle="dashed", label="Future Prediction")
ax.set_xlabel("Days")
ax.set_ylabel("Gold Price")
ax.legend()

st.pyplot(fig)

st.subheader("🔮 Predicted Gold Prices")
st.dataframe(future_df)
