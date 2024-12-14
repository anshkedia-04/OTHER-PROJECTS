import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Title
st.title("Personal Fitness Dashboard")

# Sidebar for User Inputs
st.sidebar.header("Input Details")
weight = st.sidebar.number_input("Enter your weight (kg)", min_value=20.0, max_value=200.0, step=0.1)
height = st.sidebar.number_input("Enter your height (cm)", min_value=100.0, max_value=250.0, step=0.1)
goal = st.sidebar.selectbox("Select your goal", ["Weight Loss", "Muscle Gain", "Maintenance"])

# BMI Calculation
if height > 0:
    bmi = weight / ((height / 100) ** 2)
    st.sidebar.write(f"Your BMI: {bmi:.2f}")
    if bmi < 18.5:
        st.sidebar.write("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        st.sidebar.write("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        st.sidebar.write("Category: Overweight")
    else:
        st.sidebar.write("Category: Obese")

# Workout Routine Based on Goal
st.header("Weekly Workout Routine")
if goal == "Weight Loss":
    routine = ["Cardio: 30 mins", "Strength Training: 20 mins", "Yoga: 15 mins"]
elif goal == "Muscle Gain":
    routine = ["Strength Training: 45 mins", "Cardio: 15 mins", "Stretching: 10 mins"]
else:
    routine = ["Moderate Cardio: 30 mins", "Strength Training: 30 mins", "Yoga: 20 mins"]

for day, activity in zip(["Monday", "Wednesday", "Friday"], routine):
    st.write(f"{day}: {activity}")

# Weight Tracking
st.header("Track Your Weight")
if "weight_data" not in st.session_state:
    st.session_state["weight_data"] = []

if st.button("Add Weight Entry"):
    st.session_state["weight_data"].append({"Date": datetime.now().strftime("%Y-%m-%d"), "Weight": weight})

# Display Weight Data and Plot Progress
if st.session_state["weight_data"]:
    df = pd.DataFrame(st.session_state["weight_data"])
    st.write("Weight Entries:", df)

    # Plot Weight Progress
    st.subheader("Progress Chart")
    plt.figure(figsize=(10, 5))
    plt.plot(pd.to_datetime(df["Date"]), df["Weight"], marker="o", label="Weight")
    plt.xlabel("Date")
    plt.ylabel("Weight (kg)")
    plt.title("Weight Progress Over Time")
    plt.legend()
    st.pyplot(plt)

st.caption("Note: Ensure consistency in entering data for accurate tracking.")
