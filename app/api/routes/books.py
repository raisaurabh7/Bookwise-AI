from fastapi import APIRouter, HTTPException, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_session
from app.database import get_session as  get_db
# from app.database import get_db
# from app import models
from app.models.book import Book, Review
# from app.schemas import BookCreate, BookUpdate, BookOut
from app.schemas.book_schemas import BookCreate, BookUpdate, BookOut

from app.ai.llama3_summary import generate_summary




router = APIRouter(tags=["Books"])  # Removed redundant prefix

@router.post("/", response_model=BookOut)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_session)):
    content = f"{book.title} by {book.author}, Genre: {book.genre}"
    summary =  generate_summary(content)

    new_book = Book(**book.dict(), summary=summary)
    db.add(new_book)
    await db.commit()
    await db.refresh(new_book)
    return new_book


@router.get("/", response_model=list[BookOut])
async def get_books(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Book))
    return result.scalars().all()


@router.get("/{book_id}")
async def get_book(book_id: int, db: AsyncSession = Depends(get_session)):
    book = await db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    result = await db.execute(select(Review).where(Review.book_id == book_id))
    reviews = result.scalars().all()
    avg_rating = round(sum(r.rating for r in reviews) / len(reviews), 2) if reviews else None

    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "year_published": book.year_published,
        "summary": book.summary,
        "reviews": [
            {
                "id": r.id,
                "user_id": r.user_id,
                "review_text": r.review_text,
                "rating": r.rating
            } for r in reviews
        ],
        "average_rating": avg_rating
    }


@router.post("/{book_id}/generate-summary")
async def generate_summary_by_book_id(book_id: int, db: AsyncSession = Depends(get_session)):
    book = await db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    result = await db.execute(select(Review).where(Review.book_id == book_id))
    reviews = result.scalars().all()
    review_texts = "\n".join([f"- {r.review_text} (Rating: {r.rating}/5)" for r in reviews]) or "No reviews yet."

    content = f"""
        Title: {book.title}
        Author: {book.author}
        Genre: {book.genre}

        User Reviews:
        {review_texts}
    """
    summary =  generate_summary(content)
    book.summary = summary
    await db.commit()
    await db.refresh(book)

    return {"summary": summary}
