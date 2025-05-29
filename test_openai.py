import os
import openai
from dotenv import load_dotenv

load_dotenv()  # 👈 This loads your .env file into the environment

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "user", "content": "What are the top 3 challenges CFOs face when implementing self-funded insurance?"}
  ]
)

print(response.choices[0].message["content"])

