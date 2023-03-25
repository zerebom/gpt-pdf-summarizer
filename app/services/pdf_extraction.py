from typing import BinaryIO, List, Text

from pypdf import PdfReader


def extract_text_from_pdf(pdf_bytes: BinaryIO) -> Text:
    reader = PdfReader(pdf_bytes)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
