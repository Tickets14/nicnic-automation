import streamlit as st
from PIL import Image
import io

def image_to_pdf_page():
    st.title("📄 Image to PDF Converter")
    st.subheader("Easily convert images into a single PDF!")

    # Upload multiple images
    uploaded_files = st.file_uploader(
        "📂 Upload images", 
        type=["png", "jpg", "jpeg"], 
        accept_multiple_files=True
    )

    if uploaded_files:
        images = []
        
        for uploaded_file in uploaded_files:
            img = Image.open(uploaded_file).convert("RGB")  # Convert to RGB (for PDF compatibility)
            images.append(img)

        if images:
            pdf_buffer = io.BytesIO()
            images[0].save(pdf_buffer, format="PDF", save_all=True, append_images=images[1:])
            pdf_buffer.seek(0)

            # Download button for the generated PDF
            st.download_button(
                label="📥 Download PDF",
                data=pdf_buffer,
                file_name="converted.pdf",
                mime="application/pdf"
            )

            st.success("✅ PDF created successfully!")

