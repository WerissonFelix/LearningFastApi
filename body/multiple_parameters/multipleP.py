from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

#In this case, we have two body parameters: Item and User.
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User,
    importance: Annotated[int, Body()], # We declare in this way for a singular body parameter.
    # importance: int -> This is a QUERY parameter
    q: str | None = None
):
    results = {"item_id": item_id, "item": item, "user": user, 'importance:': importance}
    if q:
        results.update({"q": q})
    return results


'''    
 
e.g:

{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}

'''