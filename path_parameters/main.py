from fastapi import FastAPI

app = FastAPI()

@app.get('/items/{item_id}')
async def road_item(item_id:int):
    return {'item_id': item_id}