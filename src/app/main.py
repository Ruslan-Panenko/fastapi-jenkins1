from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from v1.api import router_v1

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_v1)