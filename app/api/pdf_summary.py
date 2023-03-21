from fastapi import APIRouter, File, UploadFile
from app.services.conversations import Conversations

from app.services.pdf_extraction import extract_text_from_pdf
from app.services.summary_service import summarize_large_text

router = APIRouter()

@router.post("/upload_pdf/")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    conversations = Conversations()
    raw_text = extract_text_from_pdf(await pdf_file.read())
    conversations =  summarize_large_text(conversations, raw_text)
    return {"conversations": conversations}
