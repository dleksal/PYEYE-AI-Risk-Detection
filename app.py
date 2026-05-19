import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="PYEYE AI Risk Detection",
    page_icon="👁️",
    layout="wide"
)

EMOTION_RISK = {
    "Happy": 10,
    "Neutral": 20,
    "Sad": 50,
    "Fear": 70,
    "Angry": 80
}

def calculate_risk(emotion):
    return EMOTION_RISK.get(emotion, 0)

st.title("👁️ PYEYE AI Risk Detection System")
st.caption("Real-time face recognition and emotion-based risk analysis dashboard")

st.sidebar.header("Controls")
camera_status = st.sidebar.toggle("Webcam Monitoring", value=False)
threshold = st.sidebar.slider("Risk Alert Threshold", 0, 100, 60)
selected_emotion = st.sidebar.selectbox(
    "Demo Emotion",
    list(EMOTION_RISK.keys())
)

risk_score = EMOTION_RISK[selected_emotion]
face_count = 1 if camera_status else 0

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Live Monitoring Preview")

    if camera_status:
        st.info("Demo mode: Webcam monitoring is simulated in this portfolio version.")
        st.image(
            "screenshots/fear-risk-demo.jpg.jpeg",
            caption="Demo screenshot from the original capstone implementation",
            use_container_width=True
        )
    else:
        st.warning("Webcam monitoring is currently turned off.")

with col2:
    st.subheader("Detection Result")
    st.metric("Faces", face_count)
    st.metric("Emotion", selected_emotion)
    st.metric("Risk Score", f"{risk_score} / 100")

    if risk_score >= threshold:
        st.error("High risk detected. Alert required.")
    else:
        st.success("Risk level is below the alert threshold.")

st.divider()

st.subheader("Risk Score Rule")

risk_table = pd.DataFrame({
    "Emotion": list(EMOTION_RISK.keys()),
    "Risk Score": list(EMOTION_RISK.values())
})

st.dataframe(risk_table, use_container_width=True)

st.subheader("Event Log Preview")

event_log = pd.DataFrame([
    {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "face_count": face_count,
        "emotion": selected_emotion,
        "risk_score": risk_score,
        "alert": risk_score >= threshold
    }
])

st.dataframe(event_log, use_container_width=True)

st.divider()

st.subheader("Project Summary")
st.write(
    """
    PYEYE is a capstone design project that combines real-time face detection,
    emotion analysis, risk score calculation, and dashboard visualization.
    The original implementation was tested with webcam input and Raspberry Pi-based execution.
    """
)
- Webcam-based monitoring
- Event logging system
""")

st.header("Demo Preview")

st.info("This repository documents the project structure, screenshots, and implementation concept.")
