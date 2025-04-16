from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.api.deps import get_current_user
from app.schemas.review_schemas import ReviewCreate, ReviewOut
from app.services import review_service

router = APIRouter()

@router.post("/", response_model=ReviewOut)
async def post_review(
    review: ReviewCreate,
    db: AsyncSession = Depends(get_session),
    user=Depends(get_current_user)
):
    return await review_service.add_review(db, user.id, review)

@router.get("/book/{book_id}", response_model=list[ReviewOut])
async def get_reviews(book_id: int, db: AsyncSession = Depends(get_session)):
    return await review_service.get_reviews(db, book_id)
