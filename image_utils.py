from PIL import Image
import matplotlib.pyplot as plt
import streamlit as st

def load_image(uploaded_file):
    return Image.open(uploaded_file)

def display_pie_chart(data):
    labels = data.keys()
    sizes = data.values()

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    ax.axis("equal")
    st.pyplot(fig)