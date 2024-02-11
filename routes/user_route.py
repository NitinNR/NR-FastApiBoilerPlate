from typing import Any, List,Annotated
from fastapi import APIRouter,Request
from fastapi.exceptions import HTTPException
from fastapi.responses import PlainTextResponse,JSONResponse
# from fastapi.encoders import jsonable_encoder
# from pydantic.networks import EmailStr
# from sqlalchemy.orm import Session
from logger import show,error

user_router = APIRouter()


@user_router.get("/user/{user_id}")
def read_user(user_id):
    return {'users':"user_data"}

@user_router.post("/user/create")
async def create_user(request: Request):
    user_data = await request.json()
    return {'users':"user created"}

# user_router.include_router(user_router,prefix="/users")

