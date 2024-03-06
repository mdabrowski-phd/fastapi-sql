"""
local server: python3 -m uvicorn app.main:app --reload
local endpoint: http://localhost:8000 (or http://127.0.0.1:8000)

tutorial: https://fastapi.tiangolo.com/tutorial/
API platform: https://www.postman.com/
"""

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from routers import tasks, users


app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    title="Task manager API",
    description="Description of my API which is visible in the documentation",
    version="1.0.0"
)
app.include_router(tasks.router)
app.include_router(users.router)


@app.get("/", description="Test endpoint for demonstration purposes")
def root():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Hello world"})
