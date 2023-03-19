import time
from typing import Any

from fastapi import FastAPI, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from starlette.exceptions import HTTPException as StarletteHTTPException

from backend import controller, database
from backend.settings import get_environment
from backend.util import error_handlers
from backend.database.models import Base as BaseMain

app = FastAPI(
    title="Projeto Teste",
    version="0.1.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_methods=["*"],
    allow_origins=["*"],
    allow_headers=["*"],
)

app.include_router(controller.router)
app.add_exception_handler(StarletteHTTPException, error_handlers.http_exception)
app.add_exception_handler(Exception, error_handlers.generic_exception)
app.add_exception_handler(RequestValidationError, error_handlers.validation_exception_handler)


@app.on_event("startup")
def startup() -> None:
    env = get_environment()
#    database.init_database(env)
#    BaseMain.metadata.create_all(database.MAIN_ENGINE)


@app.middleware("http")
async def http_middleware(request: Request, call_next: Any) -> Response:
    request.state.time_started = time_started = time.monotonic()

    #with database.SESSION_MAKER.begin() as session:
    #    request.state.db_session = session

    response: Response = await call_next(request)
    request.state.time_ended = time_ended = time.monotonic()
    request.state.time_elapsed = time_ended - time_started

     #   if response.status_code >= status.HTTP_400_BAD_REQUEST:
     #       session.rollback()

    return response
