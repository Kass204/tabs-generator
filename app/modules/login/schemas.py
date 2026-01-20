from pydantic import BaseModel, ConfigDict

class LoginCreate(BaseModel):
    username: str
    password: str
    user_id: int

class LoginResponse(BaseModel):
    id: int
    username: str
    password: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)
