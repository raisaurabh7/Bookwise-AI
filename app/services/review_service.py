from app.models.book import Review
from app.repositories import review_repo
from app.schemas.review_schemas import ReviewCreate
from sqlalchemy.ext.asyncio import AsyncSession

async def add_review(session: AsyncSession, user_id: int, data: ReviewCreate):
    review = Review(user_id=user_id, book_id=data.book_id, review_text=data.review_text, rating=data.rating)
    return await review_repo.create_review(session, review)

async def get_reviews(session: AsyncSession, book_id: int):
    return await review_repo.get_reviews_by_book_id(session, book_id)
