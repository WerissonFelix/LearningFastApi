from fastapi import FastAPI, HTTPException

from models.productAdmin import ProductAdmin
from models.productOut import ProductOut

app = FastAPI()


products = {
    1: {
        "id": 1,
        "name": "Mechanical Keyboard",
        "price": 250.00,
        "cost": 120.00,
        "supplier": "Company X",
        "stock": 15
    },
    2: {
        "id": 2,
        "name": "Gaming Mouse",
        "price": 120.00,
        "cost": 55.10,
        "supplier": "Company Y",
        "stock": 0
    },
    3: {
        "id": 3,
        "name": "Gaming Headset",
        "price": 350.00,
        "cost": 180.00,
        "supplier": "Company Z",
        "stock": 8
    },
    4: {
        "id": 4,
        "name": "Monitor 24 inches",
        "price": 900.00,
        "cost": 600.00,
        "supplier": "Company X",
        "stock": 12
    },
    5: {
        "id": 5,
        "name": "USB-C Hub",
        "price": 150.00,
        "cost": 70.00,
        "supplier": "Company W",
        "stock": 3
    }
}

@app.get("/products/{product_id}", response_model=ProductOut)
async def get_products_regular_user(product_id: int):
    product = products.get(product_id)
    
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return product

@app.get("/adm/products/{product_id}", response_model=ProductAdmin)
async def get_products(product_id: int):
    product = products.get(product_id)    

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return product
