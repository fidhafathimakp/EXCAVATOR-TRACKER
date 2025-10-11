import streamlit as st
import pandas as pd
from datetime import datetime
st,set_page_config(page_title="Cheruvadi Earth Movers",page_icon+"logo.png")
st.image("logo.png",width=120)

st.title("Excavator Work & Wage Tracker (Cheruvadi Earth Movers)")

if 'data' not in st.session_state:
    st.session_state['data'] = []

vehicle_list = [
    "JCB 140 1", "JCB 140 2", "JCB 140 3","JCB 140 4","JCB 140 5","JCB 140 6","JCB 140 7","JCB 140 8","JCB 140 9","JCB 140 10","JCB 140 11","Excavator 225", "Volvo 80","JCB 140 12","JCB 140 13","JCB 140 14",
]

st.write("### Enter Daily Details")
vehicle = st.selectbox("Select Vehicle", vehicle_list)
date = st.date_input("Date", value=datetime.today())
starting_reading = st.number_input("Starting Reading", step=0.1)
closing_reading = st.number_input("Closing Reading", step=0.1)
mode = st.selectbox("Breaker or Bucket", ["Breaker", "Bucket"])
diesel = st.number_input("Diesel filled (Litres)", min_value=0.0, step=0.1)
advance = st.number_input("Advance", min_value=0.0, step=0.1)
shifting = st.number_input("Shifting Charge", min_value=0.0, step=0.1)
batta = st.number_input("Batta", min_value=0.0, step=0.1)
salary = st.number_input("Driver Salary", min_value=0.0, step=0.1)
remark = st.text_input("Remarks / Driver Name")

work_hours = closing_reading - starting_reading if closing_reading >= starting_reading else 0.0
breaker_hours = work_hours if mode == "Breaker" else 0
bucket_hours = work_hours if mode == "Bucket" else 0

submit = st.button("Add Entry")

if submit:
    st.session_state['data'].append({
        "Vehicle": vehicle,
        "Date": date.strftime("%Y-%m-%d"),
        "Starting": starting_reading,
        "Closing": closing_reading,
        "Breaker Hours": breaker_hours,
        "Bucket Hours": bucket_hours,
        "Diesel": diesel,
        "Advance": advance,
        "Shifting": shifting,
        "Batta": batta,
        "Salary": salary,
        "Remarks": remark,
    })
    st.success("Entry added!")

st.write("### All Entries")
if st.session_state['data']:
    df = pd.DataFrame(st.session_state['data'])
    st.dataframe(df)
    st.write("#### Totals (All Vehicles)")
    st.write(f"Total Breaker Hours: {df['Breaker Hours'].sum()}")
    st.write(f"Total Bucket Hours: {df['Bucket Hours'].sum()}")
    st.write(f"Total Diesel: {df['Diesel'].sum()} L")
    st.write(f"Total Salary: ₹{df['Salary'].sum()}")
    st.write(f"Total Shifting: ₹{df['Shifting'].sum()}")
    st.write(f"Total Batta: ₹{df['Batta'].sum()}")

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download All Data as CSV", data=csv, file_name="excavator_report.csv")
else:
    st.write("No entries yet.")

st.info("Tip: To clear data, refresh the page. For sharing and cloud saving, cloud/database setup can be added later.")
