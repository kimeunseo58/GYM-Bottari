from settings import HOST,PORT
from fastapi import FastAPI
from source import main_router
import uvicorn

app = FastAPI()
app.include_router(main_router)



if __name__=="__main__":
    uvicorn.run(app=app)#,host=HOST,port=PORT)