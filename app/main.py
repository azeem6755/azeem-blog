from fastapi import FastAPI
from . import database, routes, models

app = FastAPI()

@app.on_event("startup")
def on_startup():
    database.init_db()

app.include_router(routes.router, prefix='/api/v1')