from typing import Optional
from pydantic import BaseModel
from .schcategory import CategoryResponse
from .schauthor import AuthorResponse
class BookCreate(BaseModel):
    name: str
    category_id: int
    author_id: int
    is_active: bool

class BookResponse(BaseModel):
    id: int
    name: str
    category: Optional[CategoryResponse] = None
    author: Optional[AuthorResponse] = None
    is_active: bool
    class Config:
        orm_mode = True
class BookUpdate(BaseModel):
    name: str=None
    author_id: int=None