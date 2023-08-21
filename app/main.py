from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.router import router as api_router
from webapp.router import router as web_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_router, prefix="/api")
app.include_router(web_router)
