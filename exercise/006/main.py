from fastapi import FastAPI, Cookie, Response, HTTPException
from urllib.parse import quote, unquote
from typing import Annotated
from pydantic import ValidationError

from models.preferences import Preferences

import json

app = FastAPI()



@app.post("/preferences/")
async def set_preferences(user_preferences: Preferences, response: Response):
    response.set_cookie(
        key="user_preferences",
        value=quote(json.dumps(user_preferences.model_dump())),
        httponly=True
    )
    return {"Preferences": "Saved"}


@app.get("/preferences/")
async def get_preferences(user_preferences: Annotated[str | None, Cookie()] = None):
    if user_preferences is None:
        return {'Preferences': Preferences()}
    
    try:
        preferences_data = json.loads(unquote(user_preferences))     
        preferences = Preferences.model_validate(preferences_data)
    except (json.JSONDecodeError, ValidationError):
        raise HTTPException(
            status_code=400,
            detail="Invalid preferences cookie",
        )
    return {"Preferences": preferences}