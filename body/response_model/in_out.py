from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    '''
    response_model=UserOut -> password is not included
    '''
    return user


''' 
In this case, because the two models are different, if we annotated the function
return type as UserOut, the editor and tools would complain that we are returning
an invalid type, as those are different classes.

That's why in this example we have to declare it in the response_model parameter.

There is a solution for this problem! (See using_inheritance.py)

'''