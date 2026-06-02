
# # pip install fastapi==0.116.1
# # pip install pydantic==2.11.7
# # pip install uvicorn===0.35.0
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Union
import openai

openai.api_key = ## use a api key
openai.api_base = "https://api.groq.com/openai/v1"  # Groq-compatible base URL

app = FastAPI()

class MessageData(BaseModel):
    message: str

@app.get("/api/gets")
def gets():
    return {"message": "Groq AI Data."}

@app.post("/api/postdata")
def post_data(mess: MessageData):
    try:
        response = openai.ChatCompletion.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": mess.message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return {"response": reply}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
