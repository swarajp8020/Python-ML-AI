from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import uvicorn
import config

genai.configure(api_key = config.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
app = FastAPI()
class codeRequest(BaseModel):
    code : str

@app.get("/")
def greet():
    return {"message": "Gemini is running"}
@app.post("/review")
def review_code(request:codeRequest):
    print(f"\n--Received Code (Length : {len(request.code)})---")
    prompt = f"""
    You are a Python Expert. 
    Fix the following Python code.
    Return ONLY a JSON object with this format:
    {{ "fixed_code": "YOUR_FIXED_CODE_HERE" }}
    
    The Buggy Code:
    {request.code}
    """
    try:
        print("--Ask Gemini--")
        response = model.generate_content(prompt)
        cleaned_text = response.text.replace("```json","").replace("```","").strip()
        import json
        data = json.loads(cleaned_text)
        
        print("--- ✅ Fix Sent! ---")
        return data

    except Exception as e:
        print(f"❌ Error: {e}")
        return {"fixed_code": f"# Error processing code: {e}"}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port = 8000)