from typing import Optional
from pydantic import BaseModel
from .schbook import BookResponseDTO
from .schauthor import AuthorResponseDTO
from .schuser import UserResponseDTO
class TransactionCreateDTO(BaseModel):
    user_id: int
    book_id: int

class TransactionResponseDTO(BaseModel):
    id: int
    book: Optional[BookResponseDTO] =None
    author: Optional[AuthorResponseDTO]=None
    user: Optional[UserResponseDTO]=None