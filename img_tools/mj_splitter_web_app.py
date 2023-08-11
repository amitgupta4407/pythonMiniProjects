import streamlit as st
from PIL import Image
import io

# Function to split the image
def mj_split(img):
    width, height = img.size
    center_x = width // 2
    center_y = height // 2
    # Crop the image into 4 quadrants
    top_left = img.crop((0, 0, center_x, center_y))
    top_right = img.crop((center_x, 0, width, center_y))
    bottom_left = img.crop((0, center_y, center_x, height))
    bottom_right = img.crop((center_x, center_y, width, height))
    return [top_left, top_right, bottom_left, bottom_right]

# Streamlit app
def main():
    st.title("MJ_Splitter Tool")
    st.write("Split Midjourny /stable diffusion image in seconds")

    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        if st.button("Split Image"):
            st.write("Splitting the image...")
            split_images = mj_split(img)
            st.write("Image split completed!")

            # Arrange the segments in two rows
            col1, col2 = st.columns(2)

            # Display download buttons for the first two segments in the same row
            for i in [0,3]:
                with col1:
                    st.subheader(f"Segment {i + 1}")
                    st.image(split_images[i], use_column_width=True)
                    img_bytes = io.BytesIO()
                    split_images[i].save(img_bytes, format="PNG")
                    st.download_button(f"Download Segment {i + 1}", img_bytes.getvalue(), file_name=f"segment_{i + 1}.png")

            # Display download buttons for the last two segments in the second row
            for i in [1,2]:
                with col2:
                    st.subheader(f"Segment {i + 1}")
                    st.image(split_images[i], use_column_width=True)
                    img_bytes = io.BytesIO()
                    split_images[i].save(img_bytes, format="PNG")
                    st.download_button(f"Download Segment {i + 1}", img_bytes.getvalue(), file_name=f"segment_{i + 1}.png")

if __name__ == "__main__":
    main()
