from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

try:
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    print("Client created successfully")
except Exception as e:
    print(e)
