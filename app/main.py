import requests
import streamlit as st

from app.services.conversation import continue_conversation


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

        # 新しい UI を追加
        st.write("### Ask questions about the summary:")
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": summary},
        ]
        question = st.text_input("Type your question here")
        if st.button("Ask"):
            answer = continue_conversation(messages, question)
            st.write("### Answer:")
            st.write(answer)

if __name__ == "__main__":
    main()
