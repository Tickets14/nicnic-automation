import pandas as pd
import qrcode
import streamlit as st
import zipfile
from io import BytesIO
from urllib.parse import quote

def qr_code_generator_page():
    st.title("QR Code Generator")
    st.subheader("v1.1.0", divider="green")

    # File uploader
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

    if uploaded_file is not None:
        # Get all worksheet names
        xls = pd.ExcelFile(uploaded_file)
        sheet_names = xls.sheet_names

        # Let the user select a worksheet
        selected_sheet = st.selectbox("Select a worksheet", sheet_names)

        if selected_sheet:
            # Load the selected sheet without headers to let the user pick
            raw_df = pd.read_excel(xls, sheet_name=selected_sheet, header=None)

            # Let the user choose the row number for column headers (1-based index)
            header_row_1based = st.number_input(
                "Select the row number for column headers",
                min_value=1, max_value=len(raw_df), value=1, step=1
            )

            # Convert to 0-based index for pandas
            header_row = header_row_1based - 1  

            # Load the sheet again with the selected header row
            df = pd.read_excel(xls, sheet_name=selected_sheet, header=header_row)

            # Clean column names to remove any leading/trailing spaces
            df.columns = df.columns.str.strip()
            
            # Let the user input the base URL
            base_url = st.text_input(
                "Enter the Base URL",
                value="https://www.pawnec.com/pet-vaccination",  # Default value
                help="This will be used as the base for generating links."
            )

            # Display all column names
            st.write("📌 **Available Columns:**")
            st.write(", ".join(df.columns))

            # Let the user select columns for link generation
            selected_columns = st.multiselect(
                "Select columns to include in the generated link (order matters)", df.columns
            )

            if selected_columns and base_url:
                # Remove newline characters from selected columns
                for col in selected_columns:
                    df[col] = df[col].astype(str).str.strip().str.replace("\n", "")

                # Generate dynamic links with URL encoding
                df["Link"] = df.apply(
                    lambda row: f"{base_url}/" + "/".join(quote(str(row[col])) for col in selected_columns), axis=1
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

                        # Create a valid filename for the QR code
                        filename = f"QR_{_}.png"

                        # Generate QR code
                        qr = qrcode.make(link)

                        # Save QR code to a BytesIO buffer
                        qr_buffer = BytesIO()
                        qr.save(qr_buffer, format="PNG")
                        qr_buffer.seek(0)

                        # Add the QR code to the ZIP file
                        zip_file.writestr(filename, qr_buffer.getvalue())

                # Provide a download link for the ZIP file
                st.success("✅ QR codes generated successfully!")
                st.download_button(
                    label="📥 Download QR Codes as ZIP",
                    data=zip_buffer.getvalue(),
                    file_name="qrcodes.zip",
                    mime="application/zip"
                )
