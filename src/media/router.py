import os

from fastapi import APIRouter, UploadFile, File
from uuid import UUID

from src.media.service import PhotoServer
from src.media.schemas import PhotoSchema
from src.exeptions import UnknownPhoto
from src.trainingData.service import TrainingDataService

router = APIRouter(
    prefix="/uploadMedia",
    tags=["Uploading a photo"]
)

@router.post("/upload")
async def upload_photo(file: UploadFile = File(...)):
    name = file.filename

    UPLOAD_DIR = "static/uploads"
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    path = os.path.join(UPLOAD_DIR, name)

    await PhotoServer.create_object(name=name, path=path)

@router.get("/{photo_id}")
async def get_photo(photo_id: UUID) -> PhotoSchema:
    is_photo = await PhotoServer.find_one_or_none(id=photo_id)
    if is_photo is None:
        raise UnknownPhoto
    return is_photo

@router.delete("/{photo_id}")
async def delete_photo(photo_id: UUID):
    await PhotoServer.delete_object(model_id=photo_id)