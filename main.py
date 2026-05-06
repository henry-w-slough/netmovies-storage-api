import fastapi
import uvicorn
from Exceptions import GlobalExceptionHandler
from Controllers.MovieMetadataController import MovieMetadataController

import config
import os


app = fastapi.FastAPI()

#adding exceptions to FastAPI
GlobalExceptionHandler.register_exception_handlers(app)


#the controller for movie metadata. In __init__() it adds all it's endpoints to app
movie_metadata_controller = MovieMetadataController(app)


#without this, uvicorn runs at import time causing errors
if __name__ == "__main__":
    uvicorn.run(app, host="10.0.0.16", port=8080)