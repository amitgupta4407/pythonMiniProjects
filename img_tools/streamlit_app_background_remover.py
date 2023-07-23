import os
import streamlit as st
from rembg import remove
from PIL import Image
import io

def remove_background(image_bytes):
    # Perform background removal using rembg library
    output = remove(image_bytes)
    return output

def main():
    st.title("Background Removal App")
    st.write("Upload images to remove their background")

    uploaded_images = st.file_uploader("Choose images...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

    if uploaded_images:
        for uploaded_image in uploaded_images:
            image = Image.open(uploaded_image)
            image_rgba = image.convert("RGBA")

            with io.BytesIO() as image_bytesio:
                image_rgba.save(image_bytesio, format="PNG")
                image_bytes = image_bytesio.getvalue()

            output = remove_background(image_bytes)

            if output is not None:
                st.image(output, caption="Processed Image", use_column_width=True)
            else:
                st.write("Error: Unable to process the image. Please upload a valid image.")

if __name__ == "__main__":
    main()
