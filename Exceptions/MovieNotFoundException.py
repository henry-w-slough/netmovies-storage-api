

class MovieNotFoundException(Exception):
    def __init__(self, message:str, *args) -> None:
        """Exception thrown when a movie is not found within storage."""
        super().__init__(message, *args)

        self.message = message
        self.exit_code = 404