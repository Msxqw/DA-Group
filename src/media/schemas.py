from pydantic import BaseModel, FilePath

class MediaSchema(BaseModel):
    file: FilePath
    description: str