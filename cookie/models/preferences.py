from pydantic import BaseModel

class Preferences(BaseModel):
    theme: str
    locale: str