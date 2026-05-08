from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from .MovieExistsException import MovieExistsException
from .MovieNotFoundException import MovieNotFoundException



def register_exception_handlers(app: FastAPI):
    """Adds all exceptions handlers to FastAPI app given including custom exceptions."""


    @app.exception_handler(RequestValidationError)
    async def validation_error(request: Request, exc: RequestValidationError):
        return JSONResponse(status_code=422, content={"error": "HTTP request format is invalid.", "detail": str(exc)})
    

    @app.exception_handler(MovieNotFoundException)
    async def movie_not_found_error(request: Request, exc: MovieNotFoundException):
        return JSONResponse(status_code=exc.exit_code, content=exc.message)
    

    @app.exception_handler(MovieExistsException)
    async def movie_exists_error(request: Request, exc: MovieExistsException):
        return JSONResponse(status_code=exc.exit_code, content=exc.message)


    #general exceptions not caught previously
    @app.exception_handler(Exception)
    async def general_error(request: Request, exc: Exception):
        return JSONResponse(status_code=500, content={"error": f"Unhandled exception occurred.", "detail": str(exc)})
