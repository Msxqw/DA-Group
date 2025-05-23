from sqlalchemy import insert, select, delete
from uuid import UUID

from src.db.domain.database import async_session_maker

class BaseService:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def create_object(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
    
    @classmethod
    async def delete_object(cls, model_id: UUID):
        async with async_session_maker() as session:
            stmt = delete(cls.model).filter_by(id=model_id)
            await session.execute(stmt)
            await session.commit()