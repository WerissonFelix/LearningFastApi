from pydantic import BaseModel
from models.address import Address

class Customer(BaseModel):
    name: str
    email: str 
    address: Address