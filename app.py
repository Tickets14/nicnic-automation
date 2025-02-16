import pandas as pd
import qrcode
import os
import re
import streamlit as st
import zipfile
from io import BytesIO
from urllib.parse import quote

# Function to sanitize filenames (removes invalid characters)
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)  # Replace invalid characters with '_'

# Streamlit app
def main():
    st.title("QR Code Generator")
    st.subheader("v1.0.0")
    st.divider()
    # File uploader
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

    if uploaded_file is not None:
        # Let the user input the base URL
        base_url = st.text_input(
            "Enter the Base URL",
            value="https://www.pawnec.com/pet-vaccination",  # Default value
            help="This will be used as the base for generating links."
        )

        # Load the Excel file
        df = pd.read_excel(uploaded_file)

        # Clean column names to remove any leading/trailing spaces
        df.columns = df.columns.str.strip()

        # Display the uploaded Excel data
        st.subheader("Uploaded Excel Data")

        st.dataframe(df)  # Display the DataFrame in an interactive table


        # Generate links with URL encoding
        df["Link"] = df.apply(
            lambda row: f"{base_url}/{quote(str(row['VetId']))}/{quote(str(row['VetOrgId']))}/{quote(str(row['DrugId']))}", axis=1
        )

        # Display the DataFrame with generated links
        st.subheader("Data with Generated Links")
        st.dataframe(df)  # Show the DataFrame with the new "Link" column

        # Create a BytesIO buffer for the ZIP file
        zip_buffer = BytesIO()

        # Create a ZIP file
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # Generate QR codes and add them to the ZIP file
            for _, row in df.iterrows():
                # Construct the QR code content (URL)
                link = row["Link"]

                # Create a valid folder name for the Vet
                vet_folder = sanitize_filename(row["Vet"])
                subfolder = vet_folder  # Subfolder in the ZIP file

                # Create a valid filename for the QR code
                drug_name = sanitize_filename(row["Drug"].upper())  # Sanitize drug name
                filename = f"[{drug_name}] - {vet_folder}.png"
                file_path = os.path.join(subfolder, filename)

                # Generate QR code
                qr = qrcode.make(link)

                # Save QR code to a BytesIO buffer
                qr_buffer = BytesIO()
                qr.save(qr_buffer, format="PNG")
                qr_buffer.seek(0)

                # Add the QR code to the ZIP file
                zip_file.writestr(file_path, qr_buffer.getvalue())

        # Provide a download link for the ZIP file
        st.success("QR codes generated successfully!")
        st.download_button(
            label="Download QR Codes as ZIP",
            data=zip_buffer.getvalue(),
            file_name="qrcodes.zip",
            mime="application/zip"
        )

if __name__ == "__main__":
    main()