from pydantic import BaseModel

class Address(BaseModel):
    street: str 
    city: str
    postal_code: str 
    