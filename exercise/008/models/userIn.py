from models.userOut import UserOut

class UserIn(UserOut): 
    password: str
    is_admin: bool