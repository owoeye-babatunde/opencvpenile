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

if length >= 24:
    st.write(f"We are about 99% confident that the detected length {round(length, 2)} cm is statistically invalid. \
              Kindly take another picture, keeping a reasonable distance between you and your penis. \
              For maximum accuracy, make sure that a significant portion of the image is penis only")
    st.write(f"The detected width is {round(width, 2)} cm")

elif length > 18:
    st.write(f"Are you sure that this image is not doctored or more than 1X zoomed? the detected length is {round(length, 2)} cm")
    st.write(f"The detected width is {round(width, 2)} cm")


else:
    st.write(f"The length is {round(length, 2)} cm")
    st.write(f"The width is {round(width, 2)} cm")



