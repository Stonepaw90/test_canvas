# Imports
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

# App setup
st.title("Freeform Red Drawing Canvas")

# Load background image
bg_image_path = "drawn_house.png"  # Ensure this file exists in your working directory
try:
    bg_image = Image.open(bg_image_path)
except FileNotFoundError:
    st.error("Background image not found. Please ensure 'background.jpg' is available in the app directory.")
    bg_image = None

# Fixed settings
drawing_mode = "freedraw"
stroke_width = 3  # Fixed stroke width
stroke_color = "#FF0000"  # Red color
bg_color = None  # Transparent background
realtime_update = True

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fill color (optional)
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=bg_image,
    update_streamlit=realtime_update,
    height=500,  # Adjust height as needed
    drawing_mode=drawing_mode,
    key="red_canvas",
)

# Display the drawn image
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data, caption="Your Drawing")
