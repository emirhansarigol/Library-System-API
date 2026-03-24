from pydantic import BaseModel

class CategoryCreateDTO(BaseModel):
    name:str

class CategoryUpdateDTO(BaseModel):
    name: str

class CategoryResponseDTO(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True