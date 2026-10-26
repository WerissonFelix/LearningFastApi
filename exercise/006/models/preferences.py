from pydantic import BaseModel

class Preferences(BaseModel):
    """  
    
    Validates the user's preferences before they
    are stored in a cookie
    
    """
    
