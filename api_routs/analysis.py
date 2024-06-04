# third-party
import json
from fastapi import APIRouter, Depends, HTTPException, Response, Request, File, BackgroundTasks
from fastapi.datastructures import UploadFile
from sqlalchemy.orm import Session
from typing import Union

# own
from db_utils.db import get_db
from db_utils import crud
from utils.handlers import generate_hash_key
from .analysis_bakground_tasks import analyze_video


router = APIRouter(
    prefix="/analysis",
    tags=['analysis'],
)

@router.get("/{requestId}/", response_model=None)
async def get_result(request: Request, requestId: int, db: Session = Depends(get_db)) -> Union[HTTPException, dict]:
    result = await crud.get_result(db, requestId)
    if result is None:
        raise HTTPException(status_code=404, detail="Analysis for this Id not found")
    return result

@router.post("/")
async def post_media(request: Request, background_tasks: BackgroundTasks, media: UploadFile = File(), db: Session = Depends(get_db)) -> Response:

    file_name = await generate_hash_key()
    file_extension = media.filename.split('.')[-1]

    with open(f'media/{file_name}.{file_extension}', 'wb+') as dest:
        dest.write(media.file.read())
    db_file_id = await crud.create_file(db, f'{file_name}.{file_extension}')
    background_tasks.add_task(analyze_video, request, f'{file_name}.{file_extension}', db_file_id, db)
    return Response(status_code=200, content=json.dumps({'requestId': db_file_id}))

@router.delete("/{requestId}/")
async def delete_result(requestId: int, db: Session = Depends(get_db)) -> Response:
    pass


