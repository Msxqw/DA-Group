from pydantic import BaseModel

class VideoSchema(BaseModel):
    name: str
    path: str