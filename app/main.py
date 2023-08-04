import uvicorn
import asyncio
import logging

from app.core.di import init_di
from core.persistence import init_mongo
from fastapi import FastAPI

from route import root_router

app = FastAPI()

FORMAT = "%(levelname)s:     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

init_di()

app.include_router(root_router)


@app.on_event("startup")
async def on_startup():
    await init_mongo()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)