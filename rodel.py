import streamlit as st 
from PIL import Image

 

# Create an Image object from an Image

colorImage  = Image.open("rodel.png")
imageLocation = st.empty()
 

# Rotate it by 45 degrees
for i in range(0,1000, 5):
	rotated = colorImage.rotate(i)
	imageLocation.image(rotated)
