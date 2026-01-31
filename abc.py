import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.set_page_config(page_title="Future Gold Price Prediction", page_icon="🟡")

st.title("🟡 Future Gold Price Prediction Analysis")
st.markdown("Predict future gold prices using Machine Learning")

# User input
days = st.slider("Select number of future days to predict", 5, 30, 10)

# Load gold data
with st.spinner("Fetching historical gold data..."):
    data = yf.download("GC=F", period="1y")

data = data.reset_index()
data["Day"] = np.arange(len(data))

# Prepare ML data
X = data[["Day"]]
y = data["Close"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict future
future_days = np.arange(len(data), len(data) + days).reshape(-1, 1)
future_prices = model.predict(future_days)

# Create future dataframe
future_df = pd.DataFrame({
    "Day": future_days.flatten(),
    "Predicted Price": future_prices
})

# Plot graph
st.subheader("📈 Gold Price Prediction")

fig, ax = plt.subplots()
ax.plot(data["Day"], y, label="Historical Price")
ax.plot(future_df["Day"], future_df["Predicted Price"], 
        linestyle="dashed", label="Future Prediction")
ax.set_xlabel("Days")
ax.set_ylabel("Gold Price (USD)")
ax.legend()

st.pyplot(fig)

# Show prediction table
st.subheader("🔮 Predicted Gold Prices")
st.dataframe(future_df.tail())
