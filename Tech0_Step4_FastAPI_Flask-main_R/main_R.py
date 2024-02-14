from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    x: int



@app.post("/keisan")
def double_number(item: Item):
    return {
        "x": item.x,
        "result": 100 - abs(item.x - 60)
        }




# uvicorn main:app --reload をターミナルで実行