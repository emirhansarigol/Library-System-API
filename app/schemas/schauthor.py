from pydantic import BaseModel

class AuthorCreateDTO(BaseModel):
    name: str
class AuthorUpdateDTO(BaseModel):
    name: str

class AuthorResponseDTO(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

