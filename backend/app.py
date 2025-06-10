# AI Legal Assistant Backend

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os
import fitz  # PyMuPDF
import docx
import requests

# Load environment variables
load_dotenv()

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Gemini API setup
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Legal Assistant Backend"}

# Extract text from PDF
def extract_text_from_pdf(file_bytes):
    text = ""
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Extract text from DOCX
def extract_text_from_docx(file_bytes):
    with open("temp.docx", "wb") as f:
        f.write(file_bytes)
    doc = docx.Document("temp.docx")
    return "\n".join([para.text for para in doc.paragraphs])

# Upload endpoint
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await file.read()
        print(f"File received: {file.filename} ({len(content)} bytes)")

        if file.filename.endswith(".pdf"):
            text = extract_text_from_pdf(content)
        elif file.filename.endswith(".docx"):
            text = extract_text_from_docx(content)
        else:
            return JSONResponse(status_code=400, content={"error": "Unsupported file type"})

        headers = {"Content-Type": "application/json"}
        params = {"key": GEMINI_API_KEY}
        body = {
            "contents": [{
                "parts": [{"text": f"Summarize this legal content:\n{text[:5000]}"}]
            }]
        }

        response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=body)
        data = response.json()

        if "candidates" not in data:
            print("Gemini API failed response:", data)
            return JSONResponse(status_code=500, content={"error": "Gemini API failed", "details": data})

        answer = data["candidates"][0]["content"]["parts"][0].get("text", "No summary available.")
        return JSONResponse(status_code=200, content={"answer": answer})

    except Exception as e:
        print("Exception:", str(e))
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/health")
async def health():
    return {"status": "Backend is running"}
