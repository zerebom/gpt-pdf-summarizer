import requests
import streamlit as st

from app.services.conversation import continue_conversation


def main():
    st.title("PDF Summarizer")

    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

    if pdf_file is not None:
        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "summary" not in st.session_state:
            st.session_state.summary = handle_pdf_upload(pdf_file)
            st.session_state.messages.append({"role": "assistant", "content": st.session_state.summary})

    question = st.text_input("Type your question here")

    if st.button("Ask", key="ask_button"):
        if question:
            answer = continue_conversation(st.session_state.messages, question)
            st.session_state.messages.append({"role": "user", "content": question})
            st.session_state.messages.append({"role": "assistant", "content": answer})

    if "messages" in st.session_state:
        for message in st.session_state.messages:
            if message["role"] == "assistant":
                st.write("Assistant: ", message["content"])
            else:
                st.write("You: ", message["content"])

if __name__ == "__main__":
    main()
