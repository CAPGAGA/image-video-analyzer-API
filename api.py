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


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)



@asynccontextmanager
async def lifespan(app: FastAPI):
    app.ml_model = run_model.run_model
    yield
    del app.ml_model

# init routs
app = FastAPI(lifespan=lifespan)

# add routs
app.include_router(analysis.router)


@app.on_event('startup')
async def init_api():

    if not os.path.exists(MEDIA_PATH):
        os.makedirs(MEDIA_PATH)

    if not os.path.exists(TEMP_FILES):
        os.makedirs(TEMP_FILES)

    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)




