from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()



@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    """  
    
    Using the Header() is necessary to fastapi do not declare the 
    user_agent as a Query parameter.
    
    """
    
    return {"User-Agent": user_agent}

@app.get("/headers/")
async def read_headers(x_token: Annotated[list[str] | None, Header()] = None):
    """ 
    Using list[str] allows multiple values for the same header identifier
    """
    return {"X-Token values": x_token}