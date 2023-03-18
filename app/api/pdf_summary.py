from fastapi import APIRouter, UploadFile, File
from app.services.pdf_extraction import extract_text_from_pdf

router = APIRouter()

@router.post("/upload_pdf/")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    text = extract_text_from_pdf(await pdf_file.read())
    return {"text": text}
