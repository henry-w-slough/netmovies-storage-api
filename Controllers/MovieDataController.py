import fastapi
import uuid
import os

from Utilities import MovieDataAssembler
import config


class MovieDataController:


    def __init__(self, app:fastapi.FastAPI) -> None:
        """Handles all Movie data related HTTP requests."""
        #adding endpoints to fastapi
        app.post("/data/uploadMovieData/{storageId}")(self.uploadMovieData)


    async def uploadMovieData(self, storageId:uuid.UUID, request:fastapi.Request) -> fastapi.Response:

        movie_directory = os.path.join(config.MOVIE_ROOT_DIRECTORY, str(storageId))

        #attaching the movie data stream in the movie directory using MovieDataAssembler
        await MovieDataAssembler.assemble_data(movie_directory, request.stream())

        return fastapi.responses.JSONResponse(status_code=201, content={"storageId": {storageId}})