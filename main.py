import fastapi
import uvicorn

from Controllers import MovieDataController, MovieDirectoryController
import config


app = fastapi.FastAPI()


data_controller = MovieDataController.MovieDataController(app)
directory_controller = MovieDirectoryController.MovieDirectoryController(app)


if __name__ == "__main__":
    uvicorn.run(app, host=config.STORAGE_HOST, port=config.STORAGE_PORT)

