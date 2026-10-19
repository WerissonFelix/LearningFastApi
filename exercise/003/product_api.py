from fastapi import FastAPI, Path, Query
from typing import Annotated

app =  FastAPI()

@app.get('/products/{product_id}')
async def read_product(
    product_id: Annotated[int, Path(title="The ID of the product", ge=1, le=500)],
    weight: Annotated[float, Query(gt=0, lt=50.5)]
):
    return {"product_id": product_id, "weight": weight}