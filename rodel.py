import streamlit as st 
from PIL import Image

 

# Create an Image object from an Image
colorImage  = Image.open("rodel.png")
imageLocation = st.empty()
imageLocation.image(colorImage)


if st.button('Click to make me keep spinning!'):
	for i in range(0,1440, 5):
		rotated = colorImage.rotate(i)
		imageLocation.image(rotated)
 

# Rotate it by 45 degrees

