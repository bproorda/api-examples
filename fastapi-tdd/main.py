from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


class Item(BaseModel):
    name: str
    price: float

items = []

@app.post("/items/", status_code=201)
async def create_item(item: Item):
    item_dict = item.model_dump()
    item_dict["id"] = len(items) + 1
    items.append(item_dict)
    return item_dict