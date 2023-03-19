from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


def generic_exception() -> JSONResponse:
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return JSONResponse({"detail": [{"msg": "Internal Server Error", "type": "Exception"}]}, status_code=status_code)


def http_exception(exception: StarletteHTTPException) -> JSONResponse:
    detail = [{"msg": str(exception.detail), "type": type(exception).__name__}]
    if headers := getattr(exception, "headers", None):
        return JSONResponse({"detail": detail}, status_code=exception.status_code, headers=headers)
    return JSONResponse({"detail": detail}, status_code=exception.status_code)


def validation_exception_handler(exception: RequestValidationError) -> JSONResponse:
    errors_content = jsonable_encoder({"detail": exception.errors(), "body": exception.body})
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    return JSONResponse(content=errors_content, status_code=status_code)
