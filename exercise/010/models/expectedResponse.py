from pydantic import BaseModel, EmailStr

class ExpectedResponse(BaseModel):
    model_config = {'extra': 'ignore'}
    
    id: int
    name: str
    email: EmailStr
    active: bool
    
    
