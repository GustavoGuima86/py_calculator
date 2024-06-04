from urllib.request import Request

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.rest_controller import CalculationApi

app = FastAPI()

# Include the API routes
app.include_router(CalculationApi.router)

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )