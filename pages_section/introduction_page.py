import re
import streamlit as st

# Function to sanitize filenames (removes invalid characters)
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)  # Replace invalid characters with '_'

# Function for the Introduction Page
def introduction_page():
    st.title("📌 Welcome to Nic Nic Automation!")
    st.subheader("v2.0.0", divider="rainbow")  # Add a colorful divider
    
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 800px;
        }
        .feature-card {
            padding: 1.5rem;
            border-radius: 10px;
            background-color: #f9f9f9;
            border: 1px solid #e0e0e0;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .feature-card h3 {
            color: #4CAF50;
            margin-top: 0;
        }
        .feature-card ul {
            padding-left: 1.5rem;
        }
        .feature-card li {
            margin-bottom: 0.5rem;
        }
        hr {
            border: 1px solid #4CAF50;
            margin: 1.5rem 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        ### 📌 **Features**
        """,
        unsafe_allow_html=True
    )
    
    # Feature 1: QR Code Generator
    st.markdown(
        """
        <div class="feature-card">
            <h3>🎯 QR Code Generator</h3>
            <ul>
                <li>✅ <strong>Upload</strong> an <strong>Excel file</strong> with multiple sheets</li>
                <li>✅ <strong>Select</strong> a worksheet and specific columns for QR code generation</li>
                <li>✅ <strong>Generate dynamic links</strong> using a <strong>custom base URL</strong></li>
                <li>✅ <strong>Download</strong> all QR codes as a <strong>ZIP file</strong></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Feature 2: Image Background Remover
    st.markdown(
        """
        <div class="feature-card">
            <h3>🎨 Image Background Remover</h3>
            <ul>
                <li>✅ <strong>Upload</strong> an <strong>image</strong></li>
                <li>✅ <strong>Remove</strong> the <strong>background</strong> from the image</li>
                <li>✅ <strong>Download</strong> the <strong>processed image</strong></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Feature 3: Image to PDF Converter
    st.markdown(
        """
        <div class="feature-card">
            <h3>📄 Image to PDF Converter</h3>
            <ul>
                <li>✅ <strong>Upload</strong> multiple <strong>images</strong></li>
                <li>✅ <strong>Convert</strong> them into a single <strong>PDF</strong></li>
                <li>✅ <strong>Download</strong> the <strong>converted PDF</strong></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <hr>
        <p style="text-align: center; color: #666;">✨ Explore the features above to automate your tasks effortlessly! ✨</p>
        """,
        unsafe_allow_html=True
    )


# Call the introduction page function
introduction_page()
