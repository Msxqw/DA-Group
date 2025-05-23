import os

from fastapi import APIRouter, UploadFile, File, HTTPException, status
from uuid import UUID

from src.media.service import PhotoServer
from src.media.schemas import PhotoSchema

router = APIRouter(
    prefix="/uploadMedia"
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return is_photo

@router.delete("/{photo_id}")
async def delete_photo(photo_id: UUID):
    await PhotoServer.delete_object(model_id=photo_id)