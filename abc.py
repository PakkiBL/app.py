import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.set_page_config(page_title="Future Gold Price Prediction", page_icon="🟡")

st.title("🟡 Future Gold Price Prediction Analysis")
st.markdown("Offline Machine Learning model (No API, No Internet)")

# Sample historical gold price data
prices = [
    1850, 1852, 1855, 1853, 1858, 1862, 1865,
    1868, 1870, 1873, 1875, 1878, 1880
]

df = pd.DataFrame({"Price": prices})
df["Day"] = np.arange(len(df))

# Train ML model
X = df[["Day"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

# User input
future_days = st.slider("Select future days to predict", 5, 30, 10)

future_X = np.arange(len(df), len(df) + future_days).reshape(-1, 1)
future_prices = model.predict(future_X)

future_df = pd.DataFrame({
    "Day": future_X.flatten(),
    "Predicted Gold Price": future_prices
})

# Plot
fig, ax = plt.subplots()
ax.plot(df["Day"], y, label="Historical Price")
ax.plot(future_df["Day"], future_df["Predicted Gold Price"],
        linestyle="dashed", label="Future Prediction")
ax.set_xlabel("Days")
ax.set_ylabel("Gold Price")
ax.legend()

st.pyplot(fig)

# Output table
st.subheader("🔮 Predicted Gold Prices")
st.dataframe(future_df)
