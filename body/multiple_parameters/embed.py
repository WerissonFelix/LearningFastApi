from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

''' 
Put the model inside a JSON object with a key named item, 
instead of receiving the model directly

'''
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

''' 

In this case FastAPI will expect a body like:

{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}

instead of:


{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}


'''