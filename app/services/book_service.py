
# app/services/book_service.py
from app.models.book import Book, Review
from app.schemas.book_schemas import BookCreate, BookUpdate, ReviewCreate
from app.repositories import book_repo
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.book_schemas import SummaryRequest
from app.utils.llama_client import generate_summary_with_llama

# Book Service
async def add_book(session: AsyncSession, data: BookCreate):
    book = Book(**data.dict())
    return await book_repo.create_book(session, book)

async def get_books(session: AsyncSession):
    return await book_repo.get_all_books(session)

async def get_book(session: AsyncSession, book_id: int):
    return await book_repo.get_book_by_id(session, book_id)

async def update_book(session: AsyncSession, book_id: int, data: BookUpdate):
    book = await get_book(session, book_id)
    if book:
        for field, value in data.dict(exclude_unset=True).items():
            setattr(book, field, value)
        await session.commit()
        await session.refresh(book)
    return book

async def delete_book(session: AsyncSession, book_id: int):
    book = await get_book(session, book_id)
    if book:
        await book_repo.delete_book(session, book)
    return book

