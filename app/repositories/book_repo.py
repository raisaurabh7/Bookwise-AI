from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.book import Book, Review

# Book
async def create_book(session: AsyncSession, book: Book):
    session.add(book)
    await session.commit()
    await session.refresh(book)
    return book

async def get_all_books(session: AsyncSession):
    result = await session.execute(select(Book))
    return result.scalars().all()

async def get_book_by_id(session: AsyncSession, book_id: int):
    result = await session.execute(select(Book).where(Book.id == book_id))
    return result.scalar_one_or_none()

async def delete_book(session: AsyncSession, book: Book):
    await session.delete(book)
    await session.commit()

