from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.core.security import get_password_hash, verify_password, create_access_token
from app.schemas.user_schemas import UserCreate

async def get_user_by_email(session: AsyncSession, email: str):
    result = await session.execute(select(User).where(User.email == email))
    return result.scalars().first()

async def create_user(session: AsyncSession, user: UserCreate):
    db_user = User(email=user.email, hashed_password=get_password_hash(user.password))
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user

async def authenticate_user(session: AsyncSession, email: str, password: str):
    user = await get_user_by_email(session, email)
    if user and verify_password(password, user.hashed_password):
        return user
    return None
 
