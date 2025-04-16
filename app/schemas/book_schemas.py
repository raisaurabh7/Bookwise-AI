from typing import List, Optional
from pydantic import BaseModel

# Book
class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    year_published: int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    summary: Optional[str] = None

class BookOut(BookBase):
    id: int
    summary: Optional[str]

    class Config:
        orm_mode = True

