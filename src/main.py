from fastapi import FastAPI
from src.users.router import router as router_user
from src.media.router import router as router_media

app = FastAPI()

@app.get("/")
async def get_info():
    return "Hello"

app.include_router(router_user)
app.include_router(router_media)