import shutil
import uuid
import fastapi
import config
import os
from Utilities import DataAttacher
from Exceptions.MovieNotFoundException import MovieNotFoundException
import json



class MovieMetadataController:


    def __init__(self, app:fastapi.FastAPI) -> None:
        """Handles HTTP requests involving movie metadata that is sent."""
        
        #routing the post for create_movie_metadata through the app directly
        #we don't use a Router here because it's just overkill, we only are using the metadata temporarily
        #and have no need to combine any endpoints with the same url prefix
        app.post("/movies/{storage_id}")(self.create_movie)
        app.delete("/movies/{storage_id}")(self.delete_movie_by_storage_id)


    async def create_movie(self, storage_id:uuid.UUID, request:fastapi.Request):
        """POST handler that creates a new directory based on the UUID of the HTTP request holding the movie metadata."""
        
        movie_directory = os.path.join(config.DEFAULT_ROOT_DIR, f"{storage_id}")
        os.makedirs(movie_directory, exist_ok=True)
    
        await DataAttacher.attach_data(movie_directory, request.stream())

        return fastapi.responses.JSONResponse(status_code=201, content={"status": "Movie successfully created."})
    

    async def delete_movie_by_storage_id(self, storage_id:uuid.UUID):
        """POST handler that creates a new directory based on the UUID of the HTTP request holding the movie metadata."""

        movie_dir = os.path.join(config.DEFAULT_ROOT_DIR, str(storage_id))

        # Check if it exists BEFORE trying to create
        if not os.path.exists(movie_dir):
            raise MovieNotFoundException(f"Movie of StorageId: {storage_id} not found in database.")
        
        shutil.rmtree(movie_dir)
        
        return fastapi.responses.JSONResponse(status_code=200, content={"status": "Movie successfully deleted."})

