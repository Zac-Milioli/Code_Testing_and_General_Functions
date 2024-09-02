from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FruitEnum(str, Enum):
    apple = "apple"
    banana = "banana"
    orange = "orange"

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
def read_root():
    return {"message": "Using FastAPI"}

@app.get("/fruit/{fruit_name}")
def get_fruit(fruit_name: FruitEnum):
    return {"fruit_name": fruit_name, "message": f"You chose {fruit_name}!"}

@app.post("/items/")
def create_item(item: Item):
    total_price = item.price + (item.tax if item.tax else 0)
    return {
        "item_name": item.name,
        "total_price": total_price,
        "description": item.description,
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
