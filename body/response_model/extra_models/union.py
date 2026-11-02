from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: str = "car"


class PlaneItem(BaseItem):
    type: str = "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },

}


@app.get("/items/{item_id}", response_model=PlaneItem | CarItem | int)
async def read_item(item_id: str):
    item = items.get(item_id)
    if item_id not in ["item1", "item2"]:
        return 10
    return item


''' 

For Python 3.9 and older, we must use Union[PlaneItem, CarItem].

'''