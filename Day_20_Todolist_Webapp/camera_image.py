import streamlit as st
from PIL import Image

# PIL came as a part of streamlit package

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

uploaded_image = st.file_uploader("Upload Image")

if camera_image:  # So that time taken to allow access to camera does not cause errors.
    # Create a pillow image instance
    img = Image.open(camera_image)  # It recognizes the streamlit image and gives us a PIL image
    gray_img = img.convert("L")  # L converts to grayscale

    # Render the gray scale of the image
    st.image(gray_img)

if uploaded_image:
    # Create a pillow image instance
    img2 = Image.open(uploaded_image)  # It recognizes the streamlit image and gives us a PIL image
    gray_img2 = img2.convert("L")  # L converts to grayscale

    # Render the gray scale of the image
    st.image(gray_img2)


