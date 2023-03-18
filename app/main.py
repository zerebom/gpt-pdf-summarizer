import streamlit as st
import requests
import io

FASTAPI_URL = "http://localhost:8000"

def main():
    st.title("PDF Text Extractor")
    uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

    if uploaded_file is not None:
        response = requests.post(
            f"{FASTAPI_URL}/upload_pdf/",
            files={"pdf_file": ("pdf_file.pdf", uploaded_file.getvalue(), "application/pdf")},
        )
        response.raise_for_status()
        text = response.json()["text"]
        st.write("### Extracted Text")
        st.write(text)

if __name__ == "__main__":
    main()
