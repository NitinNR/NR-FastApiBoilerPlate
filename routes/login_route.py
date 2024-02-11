from typing import Any, List

from fastapi import APIRouter

login_router = APIRouter()

@login_router.get("/login")
def login_user() -> Any:
    return {'login status':True}