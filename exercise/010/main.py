from fastapi import FastAPI, HTTPException
from models.expectedResponse import ExpectedResponse

app = FastAPI()


external_users = {
    123: {
        "id": 123,
        "name": "John",
        "email": "john@example.com",
        "active": True
    },

    124: {
        "id": "124",
        "name": "Mary",
        "email": "mary@example.com",
        "active": "true"
    },

    125: {
        "id": 125,
        "name": "Robert",
        "email": "not-an-email",
        "active": True
    },

    126: {
        "id": 126,
        "email": "sarah@example.com",
        "active": True
    },

    127: {
        "id": 127,
        "name": "Michael",
        "email": "michael@example.com",
        "active": True,
        "internal_token": "secret123",
        "credit_card": "123456789"
    },

    128: {
        "id": 128,
        "name": "Jessica",
        "email": "jessica@example.com",
        "active": "maybe"
    },

    
    129: {},

    130: {
        "id": "abc",
        "name": "David",
        "email": "david@example.com",
        "active": True
    }
}

@app.get('/external-users/{user_id}', response_model=ExpectedResponse)
async def recive_external_user(user_id: int): 
    user = external_users.get(user_id)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user