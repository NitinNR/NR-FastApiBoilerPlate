from fastapi import FastAPI,Request
from fastapi.responses import UJSONResponse,StreamingResponse,PlainTextResponse,JSONResponse
from core import Core
from schema.request_schemas.Query import Query
from schema.response_schemas.prompt_res import PromptRes
import json
import time
import asyncio
from routes import api_router
from logger import show,error
from auths.request_auth import authenticate_user
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
app = FastAPI()
# app.add_middleware(HTTPSRedirectMiddleware)

@app.middleware("http")
async def authenticate(request: Request,call_next):
    status = authenticate_user(request)
    show(status)
    if(status['status']):
        return await call_next(request)
    else:
        return JSONResponse(status)


@app.get("/stream_test")
async def stream_test():
    return StreamingResponse(fake_video_streamer())

app.include_router(api_router, prefix="/api/v1")
