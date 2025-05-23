from pydantic import BaseModel, FilePath

class MediaSchema(BaseModel):
    file: FilePath
    description: str

class PhotoSchema(BaseModel):
    name:str
    path: str