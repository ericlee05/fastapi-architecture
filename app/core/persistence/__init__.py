import logging
import os

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.domain.todo import Todo

logger = logging.getLogger(__name__)


async def init_mongo():
    logger.info("Initializing databases with Beanie..")
    client = AsyncIOMotorClient(f"mongodb://{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}")
    await init_beanie(database=client.db_name, document_models=[Todo])
    logger.info("Complete!")
