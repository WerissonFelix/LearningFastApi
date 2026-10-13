from fastapi import FastAPI

app = FastAPI()

'''

Here, the order matters. 

The path for /users/{user_id} would match also for /users/me, "thinking"
that it's receiving a parameter user_id with a value of "me". IF
the function read_user appears before read_user_me

'''


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}