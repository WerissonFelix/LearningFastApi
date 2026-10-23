from models.order import Order


from fastapi import FastAPI

app = FastAPI()


@app.post('/orders/')
async def create_order(order: Order):
    total = 0
    for product in order.products:
        total += product.price * product.quantity
    
    if order.discount is not None:
        total = total - (total * (order.discount/100))
    
    return {'Order: ': order, 'Total: ': total}

