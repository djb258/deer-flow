# app.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
import openai

# ✅ Load .env from the current directory
load_dotenv(dotenv_path=".env")

# ✅ Pull key from loaded env
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Initialize FastAPI
app = FastAPI()

@app.post("/fire")
async def fire_quote(request: Request):
    body = await request.json()
    quote_input = body.get("quote_input", "Default quote.")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": quote_input}]
        )
        output = response.choices[0].message["content"]
    except Exception as e:
        output = f"❌ Error from OpenAI: {str(e)}"
    return {
        "source": "bash",
        "quote_input": quote_input,
        "output": output
    }
	#redploy test