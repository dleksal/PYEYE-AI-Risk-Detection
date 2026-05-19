import streamlit as st

st.set_page_config(
    page_title="PYEYE AI Risk Detection",
    page_icon="👁️",
    layout="wide"
)

st.title("PYEYE AI Risk Detection System")

st.write(
    "Real-time AI risk detection system using face recognition and emotion analysis."
)

st.header("Project Overview")

st.markdown("""
PYEYE is a capstone design project that detects faces in real time,
analyzes emotional states, and estimates risk levels through a Streamlit dashboard.
""")

st.header("Main Features")

st.markdown("""
- Real-time face recognition
- Emotion analysis
- Risk score calculation
- Streamlit dashboard visualization
- Webcam-based monitoring
- Event logging system
""")

st.header("Demo Preview")

st.info("This repository documents the project structure, screenshots, and implementation concept.")
