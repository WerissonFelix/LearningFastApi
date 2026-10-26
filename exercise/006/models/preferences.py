from pydantic import BaseModel
from typing import Literal

class Preferences(BaseModel):
    """  
    
    Validates the user's preferences before they
    are stored in a cookie
    
    """
    
    theme: Literal["light", "dark"] = "light",
    language: Literal["en", "pt", "es"] = "en",
    notifications: bool = True
    
