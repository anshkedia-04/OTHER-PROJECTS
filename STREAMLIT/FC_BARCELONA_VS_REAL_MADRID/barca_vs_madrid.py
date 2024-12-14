import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("FC BARCELONA vs REAL MADRID")

st.write("### Enter Records")

# Input columns
col1, col2 = st.columns(2)

with col1:
    st.header("Barca")
    wins1 = st.number_input("Wins1", min_value=0, value=50)
    loss1 = st.number_input("Loss1", min_value=0, value=50)
    draw1 = st.number_input("Draws1", min_value=0, value=50)

with col2:
    st.header("Madrid")
    win2 = st.number_input("Wins2", min_value=0, value=50)
    loss2 = st.number_input("Loss2", min_value=0, value=50)
    draw2 = st.number_input("Draws2", min_value=0, value=50)

# Calculate Win Ratios
fcb_ratio = wins1 / (wins1 + loss1 + draw1) if (wins1 + loss1 + draw1) > 0 else 0
rm_ratio = win2 / (win2 + loss2 + draw2) if (win2 + loss2 + draw2) > 0 else 0

st.write("### Win Ratio")
col1, col2 = st.columns(2)
col1.metric(label="Barca Win Ratio", value=f"{fcb_ratio:.2f}")
col2.metric(label="Real Madrid Win Ratio", value=f"{rm_ratio:.2f}")

# Create a graph to show progress
st.write("### Team Performance Progress")

# Generate data for the graph
matches = list(range(1, 11))  # Example: 10 matches
barca_progress = [fcb_ratio * (i / 10) for i in matches]  # Simulated progress
madrid_progress = [rm_ratio * (i / 10) for i in matches]  # Simulated progress

# Plotting the graph
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(matches, barca_progress, label="FC Barcelona", marker="o", color="blue")
ax.plot(matches, madrid_progress, label="Real Madrid", marker="o", color="red")
ax.set_title("Team Performance Over Matches")
ax.set_xlabel("Matches")
ax.set_ylabel("Win Ratio")
ax.legend()
ax.grid(True)

# Display the graph
st.pyplot(fig)
