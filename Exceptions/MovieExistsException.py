from Models.MovieMetadata import MovieMetadata

class MovieExistsException(Exception):
    def __init__(self, message:str, *args: object) -> None:
        """
        Exception raised when a movie attempted to be created already exists on disk.
        Attributes:
            message(str): The information given about the exception.
        """
        super().__init__(*args)

        self.message = message