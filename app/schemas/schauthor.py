from pydantic import BaseModel

class AuthorBase(BaseModel):
    name: str
class AuthorResponse(AuthorBase):
    id: int
    class Config:
        orm_mode = True