from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
# Notice that Field is imported directly from pydantic, not from fastapi.

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

''' 
Field(): Used inside Pydantic models to configure fields, such as validation rules,
defaults, and descriptions.

Query(): Used in FastAPI endpoint parameters to configure query parameters
from the URL.

Path(): Used in FastAPI endpoint parameters to configure path parameters
from the URL.

Body(): Used in FastAPI endpoint parameters to configure request body parameters.

'''