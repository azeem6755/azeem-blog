from fastapi import FastAPI, HTTPException
from . import database, routes, models
from .config import get_settings


app = FastAPI(root_path='/blog/')

@app.middleware("http")
async def validate_host(request, call_next):
    settings = get_settings()

    host = request.headers.get("host", "")
    if settings.allowed_hosts != ["*"] and host not in settings.allowed_hosts:
        HTTPException(status_code=400, detail="Invalid host header")
    response = await call_next(request)
    return response

@app.on_event("startup")
def on_startup():
    database.init_db()

app.include_router(routes.router, prefix='/api/v1')