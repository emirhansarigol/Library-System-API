from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
class UserResponse(UserBase):
    id: int
    class Config:
        orm_mode = True
class UserUpdate(BaseModel):
    name: str