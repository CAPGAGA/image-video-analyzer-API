from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import sessionmaker

import os
# load constants
DB_HOST:str = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT:str = os.getenv('DB_PORT', '5432')
DB_USERNAME:str = os.getenv('POSTGRES_USER', 'postgres')
DB_PASSWORD:str = os.getenv('POSTGRES_PASSWORD', 'postgres123')
DB:str = os.getenv('POSTGRES_DB', 'dev')
# create db url
DATABASE_URL:str = f'postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB}'
# create engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
# base
Base: DeclarativeMeta = declarative_base()
# async session
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False, future=True)