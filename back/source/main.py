from fastapi_utils.cbv import cbv
from config import MAIN_URL
from fastapi_utils.inferring_router import InferringRouter

main_router = InferringRouter()


@cbv(main_router)
class MainSource:
    @main_router.get(MAIN_URL)
    def get(self):
        return "Hello GYM-BOTARRI"
    
    


