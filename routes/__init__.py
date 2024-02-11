from fastapi import APIRouter

from routes import user_route,login_route,signup_route

api_router = APIRouter()

api_router.include_router(user_route.user_router, tags=["user"])
api_router.include_router(login_route.login_router, tags=["login"])
api_router.include_router(signup_route.signup_router, tags=["signup"])

