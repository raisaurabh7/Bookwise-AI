from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.book import Review

async def create_review(session: AsyncSession, review: Review):
    session.add(review)
    await session.commit()
    await session.refresh(review)
    return review

async def get_reviews_by_book_id(session: AsyncSession, book_id: int):
    result = await session.execute(select(Review).where(Review.book_id == book_id))
    return result.scalars().all()
