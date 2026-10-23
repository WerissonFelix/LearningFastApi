from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float = Field(gt=0.0)
    quantity: int = Field(gt=0)
    tags: set[str] | None = None
    