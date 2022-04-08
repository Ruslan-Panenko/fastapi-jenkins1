from fastapi import FastAPI
from v1.api import router_v1

app = FastAPI()

app.include_router(router_v1)