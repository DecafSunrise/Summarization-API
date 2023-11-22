from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title='Summarizer')

import torch
from transformers import pipeline

hf_name = 'pszemraj/led-large-book-summary'
summarizer = pipeline(
    "summarization",
    hf_name,
    device=0 if torch.cuda.is_available() else -1,
)

class TextInput(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

def summarize(input_text: str):
    # Replace this function with your custom text processing logic
    return summarizer(input_text)[0]

@app.post("/summarize/")
async def summarize_api(text_input: TextInput):
    try:
        result = summarize(text_input.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
