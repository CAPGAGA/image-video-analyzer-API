from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix="/analysis",
    tags=['analysis'],
)

