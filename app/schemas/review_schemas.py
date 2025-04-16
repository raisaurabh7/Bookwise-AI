from pydantic import BaseModel

class ReviewCreate(BaseModel):
    book_id: int
    review_text: str
    rating: float

class ReviewOut(ReviewCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True  # Use this for Pydantic v2 compatibility
