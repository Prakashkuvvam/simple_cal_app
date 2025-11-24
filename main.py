from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/calculate")
def calculate(data: Numbers):
    num1 = data.num1
    num2 = data.num2

    return {
        "sum": num1 + num2,
        "diff": num1 - num2,
        "product": num1 * num2,
        "division": num1 / num2 if num2 != 0 else "undefined"
    }
