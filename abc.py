# streamlit_crop_advisory.py

import streamlit as st

st.set_page_config(page_title="Weather Based Crop Advisory System", layout="centered")
st.title("🌾 Weather Based Crop Advisory System")

# Sidebar input
st.sidebar.header("Enter Weather Parameters")
temperature = st.sidebar.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=30.0)
rainfall = st.sidebar.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0)
humidity = st.sidebar.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0)

# Crop advisory logic
def crop_advisory(temp, rain, hum):
    crops = []
    # Simple rules (you can expand with more conditions or ML)
    if 20 <= temp <= 30 and 50 <= rain <= 150 and 50 <= hum <= 70:
        crops.append("Rice 🌾")
    if 25 <= temp <= 35 and 20 <= rain <= 100 and 40 <= hum <= 60:
        crops.append("Wheat 🌱")
    if 18 <= temp <= 32 and 30 <= rain <= 120 and 50 <= hum <= 80:
        crops.append("Maize 🌽")
    if 20 <= temp <= 28 and 100 <= rain <= 250 and 60 <= hum <= 90:
        crops.append("Sugarcane 🍬")
    if 22 <= temp <= 30 and 10 <= rain <= 50 and 30 <= hum <= 50:
        crops.append("Millets 🌾")
    
    if len(crops) == 0:
        return "No suitable crops found for the given weather conditions."
    else:
        return "Recommended Crops: " + ", ".join(crops)

# Display recommendation
st.subheader("Crop Recommendation")
advice = crop_advisory(temperature, rainfall, humidity)
st.success(advice)

# Optional: show current input
st.subheader("Input Parameters")
st.write(f"🌡 Temperature: {temperature} °C")
st.write(f"🌧 Rainfall: {rainfall} mm")
st.write(f"💧 Humidity: {humidity} %")
