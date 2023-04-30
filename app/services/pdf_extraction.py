import io
from typing import BinaryIO, List, Text

from pypdf import PdfReader


def extract_text_from_pdf(pdf_bytes: bytes) -> Text:
    with io.BytesIO(pdf_bytes) as pdf_stream:
        reader = PdfReader(pdf_stream)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text
