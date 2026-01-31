import streamlit as st
import pandas as pd

# --- Sample Data ---
data = [
    {"Product": "Baby Stroller", "Category": "Gear", "Age": "0-2 yrs", "Price": 120},
    {"Product": "Infant Car Seat", "Category": "Gear", "Age": "0-1 yrs", "Price": 150},
    {"Product": "Baby Monitor", "Category": "Safety", "Age": "0-3 yrs", "Price": 80},
    {"Product": "Teething Toy", "Category": "Toys", "Age": "0-1 yrs", "Price": 15},
    {"Product": "Feeding Bottles", "Category": "Feeding", "Age": "0-2 yrs", "Price": 25},
    {"Product": "High Chair", "Category": "Feeding", "Age": "1-3 yrs", "Price": 60},
    {"Product": "Play Gym", "Category": "Toys", "Age": "0-1 yrs", "Price": 30},
    {"Product": "Baby Blanket", "Category": "Clothing", "Age": "0-2 yrs", "Price": 20},
]

df = pd.DataFrame(data)

# --- Streamlit Interface ---
st.title("🍼 Baby Product Recommendation System")

# Select categories user likes
categories = df["Category"].unique().tolist()

selected_cats = st.multiselect(
    "Select baby product categories you like:",
    categories
)

# Filter products
if selected_cats:
    recommendations = df[df["Category"].isin(selected_cats)]
else:
    recommendations = df

st.subheader("Recommended Products")
st.table(recommendations)

# Additional filter by max price
max_price = st.slider("Select maximum price:", 0, 200, 100)

filtered = recommendations[recommendations["Price"] <= max_price]

st.subheader("Filtered by Price")
st.table(filtered)

st.write("✨ Adjust the filters to customize recommendations!")
