from fastapi import FastAPI, Query, Request, Response, Depends
from fastapi.responses import JSONResponse, PlainTextResponse
from app.routers.utils_router import utils_router
from app.utils.http_error_handler import HTTPErrorHandler
from app.routers.charts_router import charts_router
from typing import Annotated
from app.utils.cors import add_cors_middleware


app = FastAPI()

# Cors Middleware
add_cors_middleware(app)
app.add_middleware(HTTPErrorHandler)

app.include_router(prefix="/api/charts", router=charts_router)
app.include_router(prefix="/api/utils", router=utils_router)
