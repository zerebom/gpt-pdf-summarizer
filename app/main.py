import io
import streamlit as st
import requests
from PIL import Image

def main():
    st.title("PDF Summarizer")

    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

    if pdf_file is not None:
        files = {"pdf_file": pdf_file.getvalue()}
        response = requests.post("http://localhost:8000/upload_pdf/", files=files)
        response.raise_for_status()
        summary = response.json()["summary"]

        st.write("### Summary:")
        st.write(summary)

if __name__ == "__main__":
    main()
