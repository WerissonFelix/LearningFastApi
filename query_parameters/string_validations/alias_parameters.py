from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

''' 
    
alias lets you define an alternative name for a parameter
that clients use when making requests.

This is useful when you want the name in the URL to differ
from the variable name in your Python code.

'''
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results