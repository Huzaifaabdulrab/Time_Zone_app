import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# App Title
st.title("Time Zone App By Huzaifa Abdulrab")

# List of Asian Time Zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "Asia/Tokyo",
    "Asia/Dubai",
    "Asia/Kolkata",
    "Asia/Moscow",
    "Asia/Seoul",
    "Asia/Bangkok",
    "Asia/Singapore",
    "Asia/Shanghai",
    "Asia/Jakarta",
    "Asia/Manila",
    "Asia/Tehran",
    "Asia/Riyadh",
    "Asia/Baghdad",
    "Asia/Hong_Kong",
    "Asia/Kuala_Lumpur",
    "Asia/Ho_Chi_Minh",
    "Asia/Yangon",
    "Asia/Taipei",
    "Asia/Colombo",
    "Asia/Kathmandu",
    "Asia/Baku",
    "Asia/Almaty",
    "Asia/Tashkent",
    "Asia/Thimphu",
]

# Dropdown to select a single time zone
selected_time_zone = st.selectbox("Select Time Zone", TIME_ZONES)

# Multi-select dropdown for multiple time zones (default UTC & Karachi)
select_timezone = st.multiselect("Select a timezone", TIME_ZONES, default=["UTC", "Asia/Karachi"])

# Display current time for selected time zones
st.subheader("Selected Timezones")

for tz in select_timezone:
    # Get current time in the selected timezone
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"Current Time in **{tz}** is {current_time}")  

# Section for converting time between time zones
st.subheader("Convert Time Between Timezones")

# Input for selecting a time to convert
current_time = st.time_input("Current Time", value=datetime.now().time())

# Dropdowns for selecting 'From' and 'To' time zones
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Button to trigger time conversion
if st.button("Convert Time"):
    # Combine selected time with today's date and assign timezone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))

    # Convert time to the target timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    
    # Display converted time
    st.success(f"Converted Time in {to_tz} : {converted_time}")
