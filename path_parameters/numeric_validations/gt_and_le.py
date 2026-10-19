from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=100, le=1000)],
    q: str,
):
    ''' 
    gt = Greater Than
    le = Less than or Equal
    item_id > 0 and item_id <= 1000
    
    
    '''
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results