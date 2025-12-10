import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

print("--- Contacting Gemini... ---")

# ATTEMPT 1: The generic 'flash' alias (Usually the safest bet)
model = genai.GenerativeModel('gemini-flash-latest')

# IF THAT FAILS, try un-commenting this one:
# model = genai.GenerativeModel('models/gemini-2.0-flash-exp')

response = model.generate_content("Explain what Python is in 1 sentence.")

print(f"\nSwaraj Says:\n{response.text}")