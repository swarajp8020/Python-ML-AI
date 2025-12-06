import uvicorn
from fastapi import FastAPI
from utils import roll_dice, get_fortune
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Fortune Teller API Online"}
@app.get("/fortune")
def predict_my_future():
    prediction = get_fortune()
    return {"fortune" : prediction}
@app.get("/roll/{sides}")
def roll_number(sides):
    result = roll_dice(sides)
    return {"sides_requested": sides, "result": result}
if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1", port=8000)