import shutil
from uuid import UUID
import fastapi
import config
import os
from Utilities import DataAttacher
from Models.MovieMetadata import MovieMetadata
from Exceptions.MovieNotFoundException import MovieNotFoundException
import json



class MovieMetadataController:


    def __init__(self, app:fastapi.FastAPI) -> None:
        """Handles HTTP requests involving movie metadata that is sent."""
        
        #routing the post for create_movie_metadata through the app directly
        #we don't use a Router here because it's just overkill, we only are using the metadata temporarily
        #and have no need to combine any endpoints with the same url prefix
        app.post("/movies")(self.create_movie_directory)
        app.delete("/movies/{storage_id}")(self.delete_movie_by_storage_id)


    async def create_movie_directory(self, request:fastapi.Request):
        """POST handler that creates a new directory based on the UUID of the HTTP request holding the movie metadata."""
        
        request_info = await request.body()
        request_info_json = json.loads(request_info)

        movie_dir = os.path.join(config.DEFAULT_ROOT_DIR, request_info_json["storage_id"])
        os.makedirs(movie_dir, exist_ok=True)
        #async data handling for storage
        await DataAttacher.attach_data(movie_dir, request_info)
        
        return fastapi.responses.JSONResponse(status_code=201, content={"status": "Movie successfully created."})
    

    async def delete_movie_by_storage_id(self, storage_id:UUID):
        """POST handler that creates a new directory based on the UUID of the HTTP request holding the movie metadata."""

        movie_dir = os.path.join(config.DEFAULT_ROOT_DIR, str(storage_id))

        # Check if it exists BEFORE trying to create
        if not os.path.exists(movie_dir):
            raise MovieNotFoundException(f"Movie of StorageId: {storage_id} not found in database.")
        
        shutil.rmtree(movie_dir)
        
        return fastapi.responses.JSONResponse(status_code=200, content={"status": "Movie successfully deleted."})

