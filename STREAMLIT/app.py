import streamlit as st 
import time as t 
import pandas as pd
import numpy as np


#title
st.title("This is a Title")

#header
st.header("This is a header")

#sub header
st.subheader("A sub-header")

# Any information
st.info("This is a peice of information") 

# Warning message 
st.warning("This is a warning")

# To display text or to write any code
st.write("To write anything")
st.write(range(50))

# to show any error 
st.error("To show any error")

# success message 
st.success("Success message ")

# Markdown
st.markdown("Hello")
st.markdown("# Hello")
st.markdown("## Hello")
st.markdown("### Hello")

# To display an emoji
st.markdown(":moon:")
st.markdown(":dog:")

#text function
st.text("This is a text")

# to write a caption
st.caption("This is a caption")

# To display mathematical expression
st.latex(r''' a+bx^2+c ''')

# to create an image 
st.image("leo_messi.jpeg")

#Widgets

# 1) Checkbox
st.checkbox('Login')

# 2) Button
st.button("Button")

# 3) Radio button
st.radio("Radio button",["Male","Female","Other"])

# 4) Select box
st.selectbox("Select_box",["Ai","Cyber"])

# 5) Multiselect
st.multiselect("Choose a department",["Sales","MArketubg","Stores"])

# 6) Select-slider
st.select_slider("Rating",["Bad","Good","Avg","Great"])

# 7) slider
st.slider("Select a no.",0,100)

# 8) number-input
st.number_input("Pick a number",0,100)

# 9) Text input
st.text_input("Enter your email")

# 10) Date input
st.date_input("Opening ceremony")

# 11) Time input
st.time_input("What is the time")

# 12) text area
st.text_area("Welcome to the real world. it sucks")

# 13) Upload a file\
st.file_uploader("Upload your file")

#14) Colour picker
st.color_picker("Pick a colour")

# 15) Progress 
st.progress(90)

#16) Spinner - temporary waiting function 
with st.spinner("Just wait"):
    t.sleep(1)

#17) Calloons for celebrations
st.balloons()

#18) Sidebar
st.sidebar.title("Welcome to the real world")
st.sidebar.text_input("Email address")
st.sidebar.text_input("Password")
st.sidebar.button("Submit")
st.sidebar.radio("Expert",["Student","teacher"])

# 19) Data visualizaations
st.title("Bar_Chart")
data = pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
st.title("Line chart")
st.line_chart(data)
st.title("Area Chart")
st.area_chart(data)

 