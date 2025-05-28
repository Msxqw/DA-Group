from fastapi import FastAPI
from src.users.router import router as router_user
from src.media.router import router as router_media
from src.video.router import router as router_video
from src.trainingData.router import router as router_training

app = FastAPI()

@app.get("/")
async def get_info():
    return "Hello"

app.include_router(router_user)
app.include_router(router_media)
app.include_router(router_video)
app.include_router(router_training)
