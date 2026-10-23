from pydantic import BaseModel, Field
from models.customer import Customer
from models.product import Product

class Order(BaseModel):
    customer: Customer
    products: list[Product]
    discount: float = Field(default=None, ge=0, le=100)
    notes: str | None = None
    