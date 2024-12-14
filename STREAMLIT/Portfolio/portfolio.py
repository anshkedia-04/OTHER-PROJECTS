import streamlit as st


st.title("WELCOME TO MY DATA SCIENCE PORTFOLIO")
st.header("Ansh Kedia | Data Scientist & Analyst Enthusiast")

# About Me Section
st.markdown("## About Me", unsafe_allow_html=True)
st.text("I am Ansh Kedia, a data science enthusiast with a passion for turning complex data into actionable insights. "
        "My expertise spans Python, machine learning, and data visualization, driving innovative solutions from "
        "predictive models to enhancing accessibility. Always eager to tackle new challenges, I thrive on solving "
        "real-world problems and staying at the forefront of technology.")
st.text("Current Status - 3rd year B.Tech in Computer Science and Engineering with a CGPA of 8.40.")

# Resume Section
st.markdown("## My Resume", unsafe_allow_html=True)
st.file_uploader("Upload your resume")

# Skills Section
st.markdown("## Skills", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("#### Data Scientist")
    st.write("- Python")
    st.write("- Pandas")
    st.write("- Numpy")
    st.write("- Matplotlib")
    st.write("- Seaborn")
    st.write("- Scikit-Learn")
    st.write("- Machine Learning")
    st.write("- Streamlit")

with col2:
    st.markdown("#### Data Analyst")
    st.write("- Excel")
    st.write("- Tableau")
    st.write("- Power BI")
    st.write("- SQL")

with col3:
    st.markdown("#### Web-Dev")
    st.write("- HTML")
    st.write("- CSS")
    st.write("- Javascript")

with col4:
    st.markdown("#### Soft Skills")
    st.write("- Communication")
    st.write("- Teamwork")
    st.write("- Problem Solving")
    st.write("- Time Management")

# Sidebar
st.sidebar.title("Personal Details")
st.sidebar.image("leo_messi.jpeg")
st.sidebar.markdown("""
<div style="text-align: center;">
    <p><b>Name:</b> Ansh Kedia</p>
    <p><b>Email:</b> <a href="mailto:anshkedia.04@gmail.com" target="_blank">anshkedia.04@gmail.com</a></p>
    <p><b>LinkedIn:</b> <a href="https://www.linkedin.com/in/ansh-kedia-249843266" target="_blank">
        <img src="https://img.icons8.com/ios-filled/24/000000/linkedin.png" alt="LinkedIn" /></a></p>
    <p><b>GitHub:</b> <a href="https://github.com/anshkedia-04" target="_blank">
        <img src="https://img.icons8.com/ios-glyphs/24/000000/github.png" alt="GitHub" /></a></p>
</div>
""", unsafe_allow_html=True)

st.sidebar.header("Education")
st.sidebar.write("10th (CBSE): 96%")
st.sidebar.write("12th (CBSE): 87%")
st.sidebar.write("B.Tech (CSE): CGPA-8.4")

# Footer
st.markdown(
    """
    <style>
    .footer{
        position:fixed absolute;
        bottom:0px;
        left:0;
        width:100%;
        color : white;
        font-size : 20px;
        text-align:centre;
        align-items: centre;
        padding:10px;
        margin-bottom:0px;

    }
    </style>
    <div class="footer">© 2024 Ansh Kedia. All rights reserved.</div>
    """,
    unsafe_allow_html=True,
)
