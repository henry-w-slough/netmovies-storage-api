import shutil
from uuid import UUID

import fastapi
import config
import os
from Models.MovieMetadata import MovieMetadata
from Exceptions.MovieExistsException import MovieExistsException
from Exceptions.MovieNotFoundException import MovieNotFoundException


class MovieMetadataController:


    def __init__(self, app:fastapi.FastAPI) -> None:
        """Handles HTTP requests involving movie metadata that is sent."""
        
        #routing the post for create_movie_metadata through the app directly
        #we don't use a Router here because it's just overkill, we only are using the metadata temporarily
        #and have no need to combine any endpoints with the same url prefix
        app.post("/storage")(self.create_movie_directory)
        app.delete("/storage/{storage_id}")(self.delete_movie_by_storage_id)



    async def create_movie_directory(self, movie_metadata: MovieMetadata):
        """POST handler that creates a new directory based on the UUID of the HTTP request holding the movie metadata."""
        movie_dir = os.path.join(config.DEFAULT_ROOT_DIR, str(movie_metadata.storage_id))
        # Check if it exists BEFORE trying to create
        if os.path.exists(movie_dir):
            raise MovieExistsException(f"Movie of StorageID: {movie_metadata.storage_id} already exists on disk and could not be created.")
        
        # Only create if it doesn't exist
        os.makedirs(movie_dir)
        
        return fastapi.responses.JSONResponse(status_code=201, content={"status": "Movie successfully created."})
    

    async def delete_movie_by_storage_id(self, storage_id:UUID):
        """POST handler that creates a new directory based on the UUID of the HTTP request holding the movie metadata."""

        movie_dir = os.path.join(config.DEFAULT_ROOT_DIR, str(storage_id))

        # Check if it exists BEFORE trying to create
        if not os.path.exists(movie_dir):
            raise MovieNotFoundException(f"Movie of StorageId: {storage_id} not found in database.")
        
        shutil.rmtree(movie_dir)
        
        return fastapi.responses.JSONResponse(status_code=201, content={"status": "Movie successfully deleted."})