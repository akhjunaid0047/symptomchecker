from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
backend_url = os.getenv("BACKEND_URL")
client = OpenAI(api_key=api_key)
