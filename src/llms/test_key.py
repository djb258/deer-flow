from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key: {api_key if api_key else 'NOT FOUND'}")
