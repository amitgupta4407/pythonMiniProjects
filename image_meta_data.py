import streamlit as st
from PIL import Image
from PIL.ExifTags import TAGS

def get_image_metadata(image):
    try:
        with Image.open(image) as img:
            metadata = img._getexif()
            if metadata:
                metadata_dict = {TAGS[key]: value for key, value in metadata.items() if key in TAGS}
                return metadata_dict
            else:
                return None
    except Exception as e:
        return None

def main():
    st.title("Image Metadata Viewer")
    st.write("Upload an image and view its metadata")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        metadata = get_image_metadata(uploaded_image)

        if metadata:
            st.subheader("Image Metadata:")
            for key, value in metadata.items():
                st.write(f"**{key}**: {value}")
        else:
            st.warning("No metadata found for the selected image.")

if __name__ == "__main__":
    main()
