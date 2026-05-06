import fastapi
import uvicorn
import requests
from Exceptions import GlobalExceptionHandler
from Models.MovieMetadata import MovieMetadata

import config
import os


app = fastapi.FastAPI()
#adding exceptions to FastAPI
GlobalExceptionHandler.register_exception_handlers(app)


@app.post("/receive_movie_metadata")
async def receive_movie_metadata(data: MovieMetadata):

    #creating new directory based on metadata provided by HTTP
    movie_dir = os.path.join(config.DEFAULT_ROOT_DIR, data.name)
    os.makedirs(movie_dir)

    return {"status": "ok"}


#without this, uvicorn runs at import time causing errors
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)