import streamlit as st
from PIL import Image
import time
import random

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="KrishiRakshak 🌱", page_icon="🌱", layout="wide")

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("🌱 KrishiRakshak")
st.sidebar.markdown("AI-Driven Crop Disease Detection & Management")
st.sidebar.markdown("---")
language = st.sidebar.radio(
    "Language",
    ["English", "Hindi", "Kannada", "Telugu"],
    index=0,
    label_visibility="visible"
)
st.write("Selected language:", language)

# ----------------------------
# Main App
# ----------------------------
st.title("🌐 AI Crop Disease Prediction Prototype")
st.markdown("Upload a crop/leaf image to detect disease and get remedies instantly.")

# File uploader
uploaded_file = st.file_uploader("📷 Upload an image of the crop leaf", type=["jpg", "jpeg", "png"])

# Dummy disease database (you can replace with real model later)
diseases = [
    {
        "name": "Powdery Mildew",
        "remedies": [
            "Spray Neem Oil (5ml/L water)",
            "Use Sulfur Fungicide (2g/L water)",
            "Ensure proper air circulation"
        ]
    },
    {
        "name": "Leaf Spot",
        "remedies": [
            "Remove affected leaves",
            "Apply Copper Fungicide",
            "Avoid overhead irrigation"
        ]
    },
    {
        "name": "Rust",
        "remedies": [
            "Use resistant crop varieties",
            "Apply Mancozeb fungicide",
            "Rotate crops regularly"
        ]
    }
]

if uploaded_file:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Leaf Image", use_column_width=True)

    # Simulate AI analysis
    with st.spinner("🔍 Analyzing crop health..."):
        time.sleep(2)
    
    # Random dummy prediction
    prediction = random.choice(diseases)
    confidence = random.randint(85, 99)

    st.success(f"✅ Disease Detected: *{prediction['name']}* (Confidence: {confidence}%)")

    st.subheader("💊 Suggested Remedies")
    for remedy in prediction['remedies']:
        st.markdown(f"- {remedy}")

    st.subheader("📊 Additional Info")
    st.markdown("- Weather conditions favoring disease: High humidity, poor ventilation")
    st.markdown("- Recommended next steps: Monitor nearby plants for symptoms")

else:
    st.info("📥 Please upload a crop/leaf image to begin detection.")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("🌱 Prototype developed for SIH 2025 | Team KrishiRakshak")

