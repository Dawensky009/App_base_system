from fastapi import FastAPI
from database import engine, Base
import models.user # Register models for create_all
from routers import user_router, auth_router
from core.config import settings
from core.exceptions import BaseAPIException, api_exception_handler

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.add_exception_handler(BaseAPIException, api_exception_handler)

import traceback
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print(f"🔥 Global Exception: {exc}")
    traceback.print_exc()
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error", "error": str(exc)},
    )

app.include_router(user_router.router)
app.include_router(auth_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Restaurant Management API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
