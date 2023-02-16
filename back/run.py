from settings import HOST,PORT,RELOAD,WORKERS
from fastapi import FastAPI,Request,BackgroundTasks
from source import main_router
from loguru import logger
from utils import request_parse,response_parse

import asyncio
import uvicorn

app = FastAPI()
app.include_router(main_router)

@app.on_event("startup")
async def init():
    logger.add("log/BackendServer_{time:YYYY-MM-DD}.log",format="<green>{time:YYYY-MM-DD HH:mm:ss}</green>\n<blue>{message}</blue>\n")
    

@app.middleware("http")
async def watch_log(request: Request, call_next,):
    start_log = request_parse(request)
    response = await call_next(request)
    end_log = response_parse(response)
    logger.info(start_log+"\n"+end_log)
    return response

if __name__=="__main__":
    asyncio.run(uvicorn.run(
        "run:app",
        host=HOST,
        port=PORT,
        workers=WORKERS,
        reload=RELOAD,
        ))