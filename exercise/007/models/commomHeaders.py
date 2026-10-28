from pydantic import BaseModel 

class CommomHeaders(BaseModel):
    model_config = {'extra': 'forbid'}
    
    host: str
    x_request_id: str
    save_data: bool | None = None
    if_modified_since: str | None = None
    x_tag: list[str] = []
    