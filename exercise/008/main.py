from fastapi import FastAPI

from models.userIn import UserIn
from models.userOut import UserOut

app = FastAPI()


@app.post('/users/')
async def create_user(user: UserIn) -> UserOut:
    return user
    