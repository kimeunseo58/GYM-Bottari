from fastapi.responses import JSONResponse
from fastapi_utils.cbv import cbv
from config import MAIN_URL,VERSION
from fastapi_utils.inferring_router import InferringRouter

main_router = InferringRouter()


@cbv(main_router)
class MainSource:
    @main_router.get(MAIN_URL)
    def get(self):
        return JSONResponse({"value":f"Version : {VERSION}"})

    


