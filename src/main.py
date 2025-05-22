from fastapi import FastAPI
from src.users.router import router as router_user

app = FastAPI()

@app.get("/")
async def get_info():
    return "Hello"

app.include_router(router_user)