import streamlit as st
import yfinance as yf
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Crypto Trends Analyzer",
    page_icon="📈",
    layout="centered"
)

st.title("📊 Crypto Trends Analyzer")
st.markdown("Analyze real-time cryptocurrency price trends")

# Crypto selection
crypto_dict = {
    "Bitcoin (BTC)": "BTC-USD",
    "Ethereum (ETH)": "ETH-USD",
    "Ripple (XRP)": "XRP-USD",
    "Litecoin (LTC)": "LTC-USD"
}

crypto_name = st.selectbox("Select Cryptocurrency", list(crypto_dict.keys()))
crypto_symbol = crypto_dict[crypto_name]

# Time period selection
period = st.selectbox(
    "Select Time Period",
    ["1d", "5d", "1mo", "3mo", "6mo", "1y"]
)

# Fetch data
if st.button("🔍 Analyze Trend", type="primary"):
    with st.spinner("Fetching live crypto data..."):
        data = yf.download(crypto_symbol, period=period)

    if data.empty:
        st.error("Unable to fetch data. Try again later.")
    else:
        st.subheader(f"📈 {crypto_name} Price Trend")

        # Current price
        current_price = data["Close"].iloc[-1]
        previous_price = data["Close"].iloc[0]

        # Trend logic
        if current_price > previous_price:
            trend = "UP 📈"
            st.success(f"Trend: {trend}")
        else:
            trend = "DOWN 📉"
            st.error(f"Trend: {trend}")

        st.metric(
            label="Current Price (USD)",
            value=f"${current_price:.2f}",
            delta=f"{current_price - previous_price:.2f}"
        )

        # Line chart
        st.line_chart(data["Close"])

        # Data table
        with st.expander("📄 View Raw Data"):
            st.dataframe(data.tail())
