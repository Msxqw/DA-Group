from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ARRAY
from typing import Final

from src.db.domain.database import Base

SQL_EMPTY_LIST = Final[str] = "{}"

class User(Base):
    __tablename__: str = "users"

    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str]
    user_role: Mapped[set[str]] = mapped_column(ARRAY(String), default=SQL_EMPTY_LIST)
    # image_avatar: Mapped[list["ImagesByUser"]] -> Подумать над m2m-связью

class ImagesByUser(Base):
    __tablename__: str = "images_by_user"

    name: Mapped[str]
    path: Mapped[str]

class Photo(Base):
    __tablename__: str = "photos"

    name: Mapped[str]
    path: Mapped[str]

class VideoStream(Base):
    __tablename__: str = "videos"

    name: Mapped[str]
    path: Mapped[str]

class TrainingData(Base):
    __tablename__: str = "training_dates"
    
    name: Mapped[str]
    path: Mapped[str]