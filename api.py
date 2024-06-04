# third-party
from fastapi import FastAPI
from contextlib import asynccontextmanager
import os


# own
from api_routs import analysis
from db_utils import models
from db_utils.db import engine
from model import run_model
from consts import MEDIA_PATH, TEMP_FILES

# logging
import logging


# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                      level=logging.INFO)
# logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    app.ml_model = run_model.run_model
    yield
    del app.ml_model

# init app
app = FastAPI(lifespan=lifespan)

# add routs
app.include_router(analysis.router)







