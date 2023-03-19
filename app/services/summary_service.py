
import os
import textwrap

import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_summary(text: str, max_length: int = 100) -> str:
    prompt = f"下記文章を日本語で要約して:\n\n{text}\n"
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

def summarize_large_text(text: str, max_chars_per_request: int = 1000, max_summary_length: int = 100) -> str:
    wrapped_text = textwrap.wrap(text, max_chars_per_request)
    summarized_text = ""

    for chunk in wrapped_text:
        summary_chunk = generate_summary(chunk, max_summary_length)
        summarized_text += summary_chunk + " "
        break

    return summarized_text.strip()

def continue_conversation(messages: list[dict[str, str]], question: str) -> str:
    print("insert:",messages)
    messages.append({"role": "user", "content": question})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    print("continue:",response)

    answer = response.choices[0].message["content"]
    messages.append({"role": "assistant", "content": answer})

    return answer
