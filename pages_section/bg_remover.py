import streamlit as st
from rembg import remove
from PIL import Image
import io

def bg_remover_page():
    st.title("🖼️ Background Remover")
    st.subheader("Remove backgrounds from images effortlessly!", divider="rainbow")

    uploaded_file = st.file_uploader("📂 Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        # Open the uploaded image
        input_image = Image.open(uploaded_file)

        # Convert image to RGBA mode (to support transparency)
        if input_image.mode != "RGBA":
            input_image = input_image.convert("RGBA")

        # Remove background
        output_image = remove(input_image)

        # Show original and processed images
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(input_image, caption="Original Image", use_container_width=True)
        
        with col2:
            st.image(output_image, caption="Background Removed", use_container_width=True)

        # Download the processed image
        img_io = io.BytesIO()
        output_image.save(img_io, format="PNG")
        img_io.seek(0)
        print("testing")
        st.download_button(
            label="📥 Download Image",
            data=img_io,
            file_name="bg_removed.png",
            mime="image/png",
        )


bg_remover_page()