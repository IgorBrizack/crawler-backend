from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.routes.product import router as ProductRouter

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ProductRouter, tags=["Product"], prefix="/product")

@app.get("/", tags=["root"])
async def read_root():
    return{"message": "Welcome to this fantastic app!"}