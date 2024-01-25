import streamlit as st
from PIL import Image
from func import measure_length_width
#from your_model_library import style_transfer, enhance_image, generate_text

# Page title and description
st.title("Penile Length Measurement")
st.markdown("Upload your penile image")

# Image upload and preview
image = st.file_uploader("Choose an image")
print(image)
length = 0
width = 0
if image:
    #if style_choice != "None":
        #manipulated_image = style_transfer(image, style_choice)
    #else:
        #manipulated_image = enhance_image(image, brightness)
    length, width = measure_length_width(image)

st.write(f"The length is {round(length, 2)} cm")
st.write(f"The width is {round(width, 2)} cm")
