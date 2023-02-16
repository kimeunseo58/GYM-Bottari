from settings import HOST,PORT
from fastapi import FastAPI,Request
from source import main_router
from loguru import logger
from utils import request_parse

import asyncio
import uvicorn

app = FastAPI()
app.include_router(main_router)

@app.on_event("startup")
async def rm_all_dockers():
    logger.add("log/BackendServer_{time:YYYY-MM-DD}.log",format="<green>{time:YYYY-MM-DD HH:mm:ss}</green>\n<blue>{message}</blue>\n")
    logger.info(f"Server Start\n")
    

@app.middleware("http")
async def watch_log(request: Request, call_next):
    logger.info(request_parse(request))
    response = await call_next(request)
    return response



if __name__=="__main__":
    asyncio.run(uvicorn.run(app=app,host=HOST,port=PORT))