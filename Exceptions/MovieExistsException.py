from Models.MovieMetadata import MovieMetadata

class MovieExistsException(Exception):
    def __init__(self, movie_data:MovieMetadata, *args: object) -> None:
        """
        Exception raised when a movie attempted to be created already exists on disk.
        Attributes:
            movie_data (MovieMetadata): The MovieMetadata model that holds information on the movie that was attemped to be created.
        """
        super().__init__(*args)

        self.movie_data = movie_data