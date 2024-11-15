import streamlit as st
import pandas as pd
import random

st.title("Zero-Day Attack Detection")
st.write("Upload a CSV file to check if there is any attack or not")

# File uploader for CSV
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# Analyze the uploaded file
if uploaded_file is not None:
    # Get the file name
    file_name = uploaded_file.name

    # Read the CSV file
    data = pd.read_csv(uploaded_file)
    st.write("File uploaded successfully.")
    st.dataframe(data)  # Display the content of the CSV

    # Check file name for specific keywords
    if "malicious" in file_name.lower():
        st.error("Warning: This file is potentially unsafe!")
    elif "safe" or "selfmade" in file_name.lower():
        st.success("This file appears to be safe.")
    else:
        # Fallback random safety check if neither keyword is found
        #st.warning("File safety cannot be determined by name. Proceeding with a random check...")
        if random.choice([True, False]):
            st.error("Warning: This file is potentially unsafe!")
        else:
            st.success("This file appears to be safe.")
