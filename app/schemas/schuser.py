from pydantic import BaseModel

class UserCreateDTO(BaseModel):
    name: str
class UserResponseDTO(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True
class UserUpdateDTO(BaseModel):
    name: str