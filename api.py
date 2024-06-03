# third-party
from fastapi import FastAPI

# own
from api_routs import analysis

# logging
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)



# init routs
app = FastAPI()

# add routs
app.include_router(analysis.router)
