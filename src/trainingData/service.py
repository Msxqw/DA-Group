from src.db.domain.models import TrainingData
from src.Service.base import BaseService
from src.db.domain.database import async_session_maker

class TrainingDataService(BaseService):
    model = TrainingData

    @classmethod
    async def add_photo_to_training(cls, name: str, path: str):
        async with async_session_maker() as session:
            object = cls.model(name=name, path=path)
            session.add(object)
            await session.commit()
            return object