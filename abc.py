import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Crypto Trends Analyzer", page_icon="📈")

st.title("📊 Crypto Trends Analyzer (Simulation Mode)")

crypto = st.selectbox("Select Crypto", ["Bitcoin", "Ethereum", "Solana"])

if st.button("Analyze Trend"):
    with st.spinner("Analyzing live trend..."):
        time.sleep(1)

        prices = np.random.randint(20000, 30000, size=10)
        df = pd.DataFrame({"Price": prices})

        trend = "UP 📈" if prices[-1] > prices[0] else "DOWN 📉"

        st.metric("Current Price (USD)", prices[-1])
        st.success(f"Trend: {trend}")
        st.line_chart(df)
