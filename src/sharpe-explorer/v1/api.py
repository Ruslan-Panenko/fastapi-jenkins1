from fastapi import APIRouter
from v1.endpoints.metrics import router

router_v1 = APIRouter(prefix="/v1", tags=["v1"])

router_v1.include_router(router)