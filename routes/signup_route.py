from typing import Any, List,Annotated
from fastapi import APIRouter

signup_router = APIRouter()

@signup_router.post("/signup")
def signup_user() -> Any:
    return {'signup status':True}