import google.generativeai as genai
from config import GEMINI_API_KEY

# 1. Configure the key
genai.configure(api_key=GEMINI_API_KEY)

print("--- Checking Available Models ---")

# 2. List all models
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"Name: {m.name}")
except Exception as e:
    print(f"Error accessing API: {e}")