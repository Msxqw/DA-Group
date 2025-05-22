import os

from fastapi import APIRouter, UploadFile, File

from src.media.schemas import PhotoSchema
from src.media.service import PhotoServer

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