import streamlit as st
import re

st.set_page_config(page_title="Cyber Security Project", page_icon="🔐")

st.title("🔐 Cyber Security User Input System")

st.write("This project demonstrates password security and login risk detection.")

# ---------------------------
# Password Strength Function
# ---------------------------
def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@$!%*?&]", password):
        score += 1

    return score

# ---------------------------
# User Input Form
# ---------------------------
with st.form("security_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    location = st.selectbox("Login Location", ["India", "USA", "UK", "Other"])
    failed_attempts = st.number_input("Failed Login Attempts", 0, 10)
    
    submit = st.form_submit_button("Analyze Security")

# ---------------------------
# Output Section
# ---------------------------
if submit:
    st.subheader("🔍 Security Analysis")

    # Password Strength
    strength = check_password_strength(password)

    if strength <= 2:
        st.error("❌ Weak Password")
    elif strength == 3:
        st.warning("⚠ Medium Strength Password")
    else:
        st.success("✅ Strong Password")

    # Login Risk Detection
    if failed_attempts >= 3:
        st.error("🚨 High Risk: Multiple Failed Login Attempts")
    else:
        st.success("🟢 Login Attempts Normal")

    # Location Risk
    if location == "Other":
        st.warning("🌍 Unrecognized Login Location")

    st.info("✔ Security analysis completed successfully")

