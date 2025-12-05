import uvicorn
from fastapi import FastAPI

# 1. Create the App (The Server Instance)
app = FastAPI()

# 2. Define a Route (The Endpoint)
# In Java: @GetMapping("/")
# In Python: @app.get("/")
@app.get("/")
def home():
    # Return a Dictionary. 
    # FastAPI automatically converts this to JSON!
    return {"message": "Hello, I am your Python Brain", "status": "Active"}

# 3. Another Endpoint (Dynamic)
# Accepts a name in the URL: /greet/Swaraj
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Welcome to AI Engineering, {name}!"}

# 4. The Runner
# This lets you run it by clicking the 'Play' button in VS Code
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)