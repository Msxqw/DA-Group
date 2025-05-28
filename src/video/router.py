import os
from fastapi import APIRouter, File, UploadFile
from uuid import UUID

from src.video.service import VideoService
from src.video.schemas import VideoSchema
from src.exeptions import UnknownVideo


router = APIRouter(
    prefix="/uploadVideo",
    tags=["Uploading a video stream"]
)

"""Ручкка на загрузку видеопотока"""
@router.post("/upload")
async def upload_photo(file: UploadFile = File(...)):
    name = file.filename

    UPLOAD_DIR = "static/uploads"
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    path = os.path.join(UPLOAD_DIR, name)

    await VideoService.create_object(name=name, path=path)

"""Ручка на получение видеопотока"""
@router.get("/{video_id}")
async def get_video(video_id: UUID) -> VideoSchema:
    is_video = await VideoService.find_one_or_none(id=video_id)
    if is_video is None:
        raise UnknownVideo
    return is_video

"""Ручка на удаление видеопотока"""
@router.delete("/{video_id}")
async def delete_video(video_id: UUID):
    await VideoService.delete_object(model_id=video_id)