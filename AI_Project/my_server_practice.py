from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import google.generativeai as genai
import uvicorn
import config
import logging
import json

# 1. SETUP LOGGER
logging.basicConfig(
    filename='server_final.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 2. CONFIGURE AI
genai.configure(api_key=config.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI()

# 3. DEFINE THE DATA SHAPE
class CodeRequest(BaseModel):
    code: str  # Type Hint (Colon, not Equals)

    @field_validator('code')
    def check_code_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Code cannot be empty/blank!')
        return v

@app.get("/")
def greet():
    return {"message": "Gemini AI Server is Running 🟢"}

# 4. THE MAIN LOGIC
@app.post("/review")
def review_code(request: CodeRequest):
    logging.info(f"Received Request. Length: {len(request.code)}")
    
    prompt = f"""
    You are a Python Expert. Fix this code.
    Return ONLY JSON: {{ "fixed_code": "..." }}
    Code: {request.code}
    """
    
    attempts = 0
    max_retries = 2
    
    while attempts < max_retries:
        try:
            logging.info(f"Attempt {attempts + 1}...")
            response = model.generate_content(prompt)
            
            # Clean the markdown
            cleaned_text = response.text.replace("```json", "").replace("```", "").strip()
            data = json.loads(cleaned_text)
            
            logging.info("Success! Returning data.")
            return data
            
        except Exception as e:
            logging.error(f"Attempt {attempts + 1} failed: {e}")
            attempts += 1 # Increment retry count
            
    # If loop finishes, we failed
    logging.error("All retries failed.")
    return {"fixed_code": "# Error: Server busy. Try again later."}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)