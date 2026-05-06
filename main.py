import fastapi
import uvicorn
from Exceptions import GlobalExceptionHandler
from Models.MovieMetadata import MovieMetadata
from Exceptions.MovieExistsException import MovieExistsException

import config
import os


app = fastapi.FastAPI()
#adding exceptions to FastAPI
GlobalExceptionHandler.register_exception_handlers(app)


@app.post("/create_movie_metadata")
async def create_movie_metadata(movie_data: MovieMetadata):
    movie_dir = os.path.join(config.DEFAULT_ROOT_DIR, str(movie_data.movie_uuid))
    
    # Check if it exists BEFORE trying to create
    if os.path.exists(movie_dir):
        raise MovieExistsException(movie_data)
    
    # Only create if it doesn't exist
    os.makedirs(movie_dir)
    
    return {"status": "ok"}


#without this, uvicorn runs at import time causing errors
if __name__ == "__main__":
    uvicorn.run(app, host="10.0.0.16", port=8080)