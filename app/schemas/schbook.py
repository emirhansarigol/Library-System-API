from typing import Optional
from pydantic import BaseModel
from .schcategory import CategoryResponseDTO
from .schauthor import AuthorResponseDTO
class BookCreateDTO(BaseModel):
    name: str
    category_id: int
    author_id: int
    is_active: bool

class BookResponseDTO(BaseModel):
    id: int
    name: str
    category: Optional[CategoryResponseDTO] = None
    author: Optional[AuthorResponseDTO] = None
    is_active: bool
    class Config:
        from_attributes = True
class BookUpdateDTO(BaseModel):
    name: str=None
    author_id: int=None
    category_id: int=None