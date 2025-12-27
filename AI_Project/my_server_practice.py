from fastapi import FastAPI, HTTPExeption
from pydantic import BaseModel, field_validator
import google.generativeai as genai
import uvicorn
import config
import logging

logging.basicConfig(
    filename = 'server_Dec27.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)
genai.configure(api_key=config.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
app = FastAPI()
class codeRequest(BaseModel):
    code : str
    @field_validator('code')
    def check_code_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Code cannot be empty/blank!')
        return v
@app.get("/")
def greet():
    return{"message":"Gemini AI Server is running"}
@app.post("/review")
def review_code(request : codeRequest):
    logging.info(f"\n--received code (Length: {len(request.code)})--")
    prompt = f"""
    You are a Python Expert. 
    Fix the following Python code.
    Return ONLY a JSON object with this format:
    {{ "fixed_code": "YOUR_FIXED_CODE_HERE" }}
    
    The Buggy Code:
    {request.code}
    """
    attempts = 0
    max_retries = 2
    while attempts < max_retries:
        try:
            logging.info("--gemini--")
            response = model.generate_content(prompt)
            cleaned_text = response.text.replace("``json","").replace("```","").strip()
            import json
            data = json.loads(cleaned_text)
            logging.info("--fix sent--")
            return data
        except Exception as e:
            logging.error(f"Error: {e}")
            return{"fixed_code": "# Error: AI could not generate valid JSON after retries."}
if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)
