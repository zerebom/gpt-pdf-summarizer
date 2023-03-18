from fastapi import FastAPI, UploadFile, File
from app.services.pdf_extraction import extract_text_from_pdf

app = FastAPI()

@app.post("/upload_pdf/")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    text = extract_text_from_pdf(await pdf_file.read())
    return {"text": text}
