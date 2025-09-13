from fastapi import FastAPI, HTTPException
from config import client
from models import SymptomRequest
from prompt import SYSTEM_PROMPT
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Symptom Checker", version="1.0")

origins = [
    "http://localhost:3000",
    "http://localhost:4040"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/check_symptoms")
async def check_symptoms(request: SymptomRequest):
    try:
        lang_hint = f"Respond in {request.language}." if request.language.lower() != "english" else ""
        response = client.responses.create(
            model="gpt-4o-mini",
            instructions=SYSTEM_PROMPT,
            input=f"Symptoms: {request.symptoms}, language: {lang_hint}",
            max_output_tokens=400,
            temperature=0.5
        )
        return {"response": response.output_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
