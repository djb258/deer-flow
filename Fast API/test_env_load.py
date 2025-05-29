import os
from dotenv import load_dotenv
from pathlib import Path

# Resolve the .env path from Fast API/
env_path = Path(__file__).resolve().parents[0] / ".env"
print("📄 Attempting to load .env from:", env_path)

load_dotenv(dotenv_path=env_path)

# Check what we got
print("🔐 OPENAI KEY LOADED:", os.getenv("OPENAI_API_KEY"))
