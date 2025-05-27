import streamlit as st
from solar_analysis import analyze_image
from image_utils import load_image, display_pie_chart

st.set_page_config(page_title="Solar Industry AI Assistant", layout="centered")
st.title("☀️ Solar Industry AI Assistant")

uploaded_file = st.file_uploader("Upload a satellite rooftop image", type=["jpg", "png", "jpeg", "webp"])

if uploaded_file:
    image = load_image(uploaded_file)
    st.image(image, caption="Uploaded Rooftop", use_container_width=True)

    if st.button("Analyze Solar Potential"):
        with st.spinner("Analyzing..."):
            result = analyze_image(image)
            st.success("Analysis Complete!")

            st.subheader("📊 Analysis Summary")
            st.write(result["summary"])

            st.subheader("💡 Installation Recommendation")
            st.write(result["recommendation"])

            st.subheader("💰 ROI Estimate")
            st.write(f"Estimated ROI: {result['roi']} years")

            st.subheader("🔍 Energy Contribution")
            display_pie_chart(result["energy_breakdown"])