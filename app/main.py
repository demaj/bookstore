from fastapi import FastAPI
from routers import books


app = FastAPI(
    title="Bookstore API",
    description="Online Bookstore API",
    version="0.1.0"
)


@app.get("/", summary="Status")
async def index():
    return {"status": "OK"}


"""
@app.on_event("startup")
async def on_startup():
    await database.connect()


@app.on_event("startup")
async def on_shutdown():
    await database.disconnect()
"""


app.include_router(books.router)
