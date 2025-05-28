from pydantic import BaseModel

class TrainingDataSchema(BaseModel):
    name: str
    path: str