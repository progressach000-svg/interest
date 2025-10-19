import streamlit as st
from nepali_datetime import date

# --- App Title ---
st.title("💰 Nepali Date Interest Calculator")

st.markdown("This app calculates simple interest based on Nepali (BS) dates and principal amount.")

# --- Input Section ---
st.subheader("📅 Enter Dates in Bikram Sambat (BS)")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Past Date (BS)**")
    year1 = st.number_input("Past Year", min_value=2000, max_value=2090, value=2080)
    month1 = st.number_input("Past Month", min_value=1, max_value=12, value=1)
    day1 = st.number_input("Past Day", min_value=1, max_value=32, value=1)

with col2:
    st.markdown("**Present Date (BS)**")
    year2 = st.number_input("Present Year", min_value=2000, max_value=2090, value=2081)
    month2 = st.number_input("Present Month", min_value=1, max_value=12, value=1)
    day2 = st.number_input("Present Day", min_value=1, max_value=32, value=1)

# --- Amount and Rate Input ---
st.subheader("💵 Enter Financial Details")

P = st.number_input("Principal Amount (Rs.)", min_value=0.0, value=10000.0, step=100.0)
R = st.number_input("Rate of Interest (%)", min_value=0.0, value=13.0, step=0.1)

# --- Calculate Button ---
if st.button("Calculate Interest"):
    try:
        # Convert input dates to Nepali date objects
        bs1 = date(year1, month1, day1)
        bs2 = date(year2, month2, day2)

        # Calculate time difference
        days_diff = (bs2 - bs1).days
        T = days_diff / 365  # years

        # Break time into years, months, days
        year_due = days_diff // 365
        month_due = (days_diff % 365) // 30
        rem_days = (days_diff % 365) % 30

        # Calculate interest
        interest = P * T * (R / 100)

        # --- Display Results ---
        st.success("✅ Calculation Complete!")

        st.write(f"🗓️ **Total Days of Interest:** {days_diff} days")
        st.write(f"📅 **Equivalent Duration:** {year_due} years, {month_due} months, {rem_days} days")
        st.write(f"💸 **Principal:** Rs. {P:,.2f}")
        st.write(f"📈 **Rate:** {R}%")
        st.info(f"💰 **Total Interest:** Rs. {interest:,.2f}")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
