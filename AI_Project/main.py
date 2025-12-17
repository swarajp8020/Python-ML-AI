# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from config import GEMINI_API_KEY

# 1. Initialize the App
app = FastAPI()

# 2. Configure AI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-flash-latest')

# 3. Define the Input Format (The "Shape" of the data)
# We expect a JSON object like: { "code": "print('hello')" }
class CodeRequest(BaseModel):
    code: str

# 4. Create the Endpoint (The "Door" to your API)
@app.post("/review")
async def review_code(request: CodeRequest):
    print("--- Received Code for Review ---")
    
    # Prepare the prompt
    prompt = f"Fix this python code and add a one liner funny comment explaining the bug:\n{request.code}"
    
    # Ask Gemini
    response = model.generate_content(prompt)
    
    # Return the result as JSON
    return {"fixed_code": response.text}

# 5. Root Endpoint (Just to check if server is alive)
@app.get("/")
def home():
    return {"message": "DevGuard API is Online! 🛡️"}