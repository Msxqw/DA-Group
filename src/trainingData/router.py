from fastapi import APIRouter

from src.trainingData.schemas import TrainingDataSchema
from src.trainingData.service import TrainingDataService

router = APIRouter(
    prefix="/training",
    tags=["Training"],
)

@router.post("/addTraining")
async def add_training_data(data: TrainingDataSchema):
    object = await TrainingDataService.add_photo_to_training(name=data.name, path=data.path)
    return {"status": "success", 
            "data": {"id": object.id,
                     "name": object.name,
                     "path": object.path
                     }
            }