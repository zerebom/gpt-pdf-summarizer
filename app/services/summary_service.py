import os
import textwrap
from typing import Optional

import openai
import streamlit as st

from .conversations import Conversations


@st.cache_resource
def set_openai_api_key(API_KEY: Optional[str] = None):

    if 'OPENAI_API_KEY' in os.environ:
        openai.api_key = os.environ.get("OPENAI_API_KEY")

    if API_KEY is not None:
        openai.api_key = API_KEY

    print("set API_KEY: ", openai.api_key)

def generate_summary(text: str, max_length: int = 100) -> str:
    # The max_lenght parameter is now ignored.
    prompt = f"Summarize this document :\n\n{text}\n"
    print(prompt)

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    )

    summary = completion.choices[0].message["content"]
    return summary

def summarize_large_text(conversations: Conversations,
                         text: str,
                         max_summarize_chars: int = 9000,
                         max_chars_per_request: int = 4000,
                         summary_length: int = 1000) -> Conversations:
    wrapped_text = textwrap.wrap(text, max_chars_per_request)
    length =  max_summarize_chars // max_chars_per_request
    wrapped_text = wrapped_text[:length]

    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for idx, chunk in enumerate(wrapped_text):
        my_bar.progress(idx, text=progress_text)
        summary_chunk = generate_summary(chunk, summary_length)
        conversations.add_message("user", f"summarize: {chunk}")
        conversations.add_message("assistant", summary_chunk)

    return conversations


def continue_conversation(conversations: Conversations, question: str) -> Conversations:
    conversations.add_message("user", question)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= conversations.get_message_dict_list()
    )

    answer = response.choices[0].message["content"]
    conversations.add_message("assistant", answer)

    return conversations