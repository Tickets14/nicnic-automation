import pandas as pd
import qrcode
import os
import re
import streamlit as st
import zipfile
from io import BytesIO
from urllib.parse import quote
from pages.qr_code_generator import qr_code_generator_page


# Function to sanitize filenames (removes invalid characters)
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)  # Replace invalid characters with '_'

# Function for the Introduction Page
def introduction_page():
    st.title("📌 Welcome to Nic Nic Automation!")
    st.subheader("v1.1.0", divider="green")

    st.markdown(
        """
        <style>
        /* Improve readability */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 800px;
        }
        hr {
            border: 1px solid #4CAF50;
        }
        </style>

        ## 🚀 **Welcome to the Multi-Tool Web App!**
        A simple and efficient tool for generating QR codes and more.

        <hr>

        ### 📌 **Features**
  
        #### 🎯 **QR Code Generator**
        ✅ **Upload** an **Excel file** with multiple sheets  
        ✅ **Select** a worksheet and specific columns for QR code generation  
        ✅ **Generate dynamic links** using a **custom base URL**  
        ✅ **Download** all QR codes as a **ZIP file**  
        <hr>

        #### 🎨 **Image Background Remover** 
        🚧 *(Coming Soon! Stay tuned for updates.)*

        """,
        unsafe_allow_html=True
    )


# Function for the QR Code Generator Page

# Streamlit Multi-Page Navigation with Sidebar Buttons
def main():
    st.sidebar.title("📌 Navigation")

    # Sidebar navigation with radio buttons
    selected_page = st.sidebar.radio("Go to:", ["🏠 Home", "📷 QR Code Generator", "🎨 BG Remover"])

    # Display the selected page
    if selected_page == "🏠 Home":
        introduction_page()
    elif selected_page == "📷 QR Code Generator":
        qr_code_generator_page()
    elif selected_page == "🎨 BG Remover":
        print("something")

if __name__ == "__main__":
    # Hide unnecessary UI elements
    st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)

    main()