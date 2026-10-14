from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    ''' 
    
    In this case, item_id is a path parameter, but q is a query parameter.

    Note that for a function parameter to be a path parameter, the variable
    in the path must have exactly the same name as the corresponding function
    parameter.

    On the other hand, for a function parameter to be a query parameter, its name
    must not correspond to a variable in the path.
    
    '''
    
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/item/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
