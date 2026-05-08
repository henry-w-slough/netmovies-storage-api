from Models.MovieMetadata import MovieMetadata

class MovieExistsException(Exception):
    def __init__(self, message:str, *args) -> None:
        """
        Exception raised when a movie attempted to be created already exists on disk.
        Attributes:
            message(str): The information given about the exception.
        """
        super().__init__(message, *args)
        
        self.message = message
        self.exit_code = 409