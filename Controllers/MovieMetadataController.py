import fastapi
import config
import os
from Models.MovieMetadata import MovieMetadata
from Exceptions.MovieExistsException import MovieExistsException


class MovieMetadataController:


    def __init__(self, app:fastapi.FastAPI) -> None:
        """Handles HTTP requests involving movie metadata that is sent."""
        
        #routing the post for create_movie_metadata through the app directly
        #we don't use a Router here because it's just overkill, we only are using the metadata temporarily
        #and have no need to combine any endpoints with the same url prefix
        app.post("/netmovies-api")(self.create_movie_directory)



    async def create_movie_directory(self, movie_data: MovieMetadata):
        """POST handler that creates a new directory based on the UUID of the HTTP request holding the movie metadata."""
        movie_dir = os.path.join(config.DEFAULT_ROOT_DIR, str(movie_data.movie_uuid))
        
        # Check if it exists BEFORE trying to create
        if os.path.exists(movie_dir):
            raise MovieExistsException(movie_data)
        
        # Only create if it doesn't exist
        os.makedirs(movie_dir)
        
        return {"status": "ok"}