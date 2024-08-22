from fastapi import FastAPI
from doclearn.api.routes import router

app = FastAPI()

app.include_router(router)
