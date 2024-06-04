from .db import async_session
from sqlalchemy.future import select

from . import models

# create new result
async def create_result(db: async_session, file_id:int, result: str) -> dict:
    new_result = models.Results(file_id=file_id,result=result)
    async with db as session:
        session.add(new_result)
        await session.commit()
        await session.refresh(new_result)
        return {'requestId': new_result.id}

# get result from db by result's id
async def get_result(db: async_session, result_id: int) -> dict:
    async with db as session:
        result = await session.execute(select(models.Results).where(models.Results.file_id == result_id))
        response = result.scalars().all()
        return response

# delete result
async def delete_result(db: async_session, result_id:int) -> dict:
    async with db as session:
        results = await session.execute(select(models.Results).where(models.Results.file_id == result_id))
        results = results.scalars().all()
        if not results:
            return {'results': 'not found'}
        for result in results:
            await session.delete(result)
        await session.commit()
        return {'results': 'deleted'}

# add new file
async def create_file(db: async_session, file_name: str) -> dict:
    new_file = models.UploadedFile(file_name=file_name)
    async with db as session:
        session.add(new_file)
        await session.commit()
        await session.refresh(new_file)
        response = new_file.id
        return response