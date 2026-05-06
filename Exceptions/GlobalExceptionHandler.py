from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from .MovieExistsException import MovieExistsException



def register_exception_handlers(app: FastAPI):
    """Adds all exceptions handlers to FastAPI app given including custom exceptions."""

    #exception for invalid http responses with invalid fields
    @app.exception_handler(RequestValidationError)
    async def validation_error(request: Request, exc: RequestValidationError):
        return JSONResponse(status_code=422, content={"error": "HTTP request format is invalid.", "detail": str(exc)})
    

    @app.exception_handler(MovieExistsException)
    async def movie_exists_error(request: Request, exc: MovieExistsException):
        return JSONResponse(status_code=409, content={"error": "Movie requested for creation already exists on disc and could not be created", "detail": f"Movie UUID: {exc.movie_data.movie_uuid}, Movie Name: {exc.movie_data.name}"})


    #handles all exceptions generally
    @app.exception_handler(Exception)
    async def general_error(request: Request, exc: Exception):
        return JSONResponse(status_code=500, content={"error": f"Unhandled exception occurred.", "detail": str(exc)})
