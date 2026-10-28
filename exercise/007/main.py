from fastapi import FastAPI, Header
from typing import Annotated

from models.commomHeaders import CommomHeaders


app = FastAPI()


@app.get("/items/")
async def get_items(
    x_request_id: Annotated[str, Header()],
    user_agent: Annotated[str | None, Header()] = None,
    accept_language: Annotated[str | None, Header()] = None,
):
    return  {
        "x-request-id": x_request_id,
        "user-agent": user_agent,
        "accept-language": accept_language
    }

@app.get("/items/headers/")
async def get_models(header: Annotated[CommomHeaders, Header()] ):
    return header.model_dump()

