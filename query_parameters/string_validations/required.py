from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

''' 
In this case, we are using Query to specify the minimum length of q. 
The parameter is required because we haven't declared a default value.

Even though q can be None according to its type annotation, 
the client need to send a value, even if the value is None.
The parameter is required simply because we haven't provided a default value.

'''
