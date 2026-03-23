from pydantic import BaseModel

class TransactionCreate(BaseModel):
    user_id: int
    book_id: int

class TransactionResponse(BaseModel):
    id: int
