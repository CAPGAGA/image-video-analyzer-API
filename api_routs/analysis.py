# third-party
from fastapi import APIRouter, Depends, HTTPException, Response, Request
from fastapi.datastructures import UploadFile
from sqlalchemy.orm import Session
from typing import Union


# own
from db_utils.db import get_db
from db_utils import crud


router = APIRouter(
    prefix="/analysis",
    tags=['analysis'],
)

@router.get("/{requestId}/", response_model=None)
async def get_result(request: Request, requestId: int, db: Session = Depends(get_db)) -> Union[HTTPException, dict]:
    result = await crud.get_result(db, requestId)
    result2 = request.app.ml_model(requestId)
    print(result2)
    if result is None:
        raise HTTPException(status_code=404, detail="Analysis for this Id not found")
    return result

@router.post("/")
async def post_media(media: UploadFile, db: Session = Depends(get_db)) -> Response:
    pass

@router.delete("/{requestId}/")
async def delete_result(requestId: int, db: Session = Depends(get_db)) -> Response:
    pass