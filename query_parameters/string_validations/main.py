from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Annotated[         # validation  validation     regular expression
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None,
):
    ''' 
    Regular expression:
        ^: starts with the following characters, doesn't have characters before.
        fixedquery: has the exact value fixedquery.
        $: ends there, doesn't have any more characters after fixedquery
    '''
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''
Default values:
def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery")
'''