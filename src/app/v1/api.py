from fastapi import APIRouter
from v1.endpoints.metrics import router as metrics_router
from v1.endpoints.description import router as description_router
from v1.token_categories import router as token_categories_router

router_v1 = APIRouter(prefix="/api/v1", tags=["v1"])

router_v1.include_router(metrics_router)
router_v1.include_router(description_router)
router_v1.include_router(token_categories_router)
