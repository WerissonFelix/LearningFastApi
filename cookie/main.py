from typing import Annotated

from fastapi import Cookie, FastAPI

from models.cookie import Cookies
from models.preferences import Preferences

app = FastAPI()


@app.get("/cookies/")
async def read_cookies(cookie: Annotated[Cookies, Cookie()]):
    return {"Cookie": cookie}


@app.get("/preferences/")
async def read_preferences(preference: Annotated[Preferences, Cookie()]):
    return {"Preference: ": preference}



