from fastapi import FastAPI
from core import deps
from routers import login, users, books
from core.database import database

app = FastAPI(
    title="Bookstore API",
    description="Online Bookstore API with JWT authentication",
    version="0.1.0"
)


@app.get("/", summary="Status")
async def index():
    """ Show application status """
    return {"status": "OK"}


@app.on_event("startup")
async def on_startup():
    await database.connect()


@app.on_event("startup")
async def on_shutdown():
    await database.disconnect()


app.include_router(login.router)
app.include_router(users.router)
app.include_router(books.router)
