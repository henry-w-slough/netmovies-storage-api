


class MovieNotFoundException(Exception):
    

    def __init__(self, message:str, *args: object) -> None:
        """Exception thrown when a requested Movie is not found within storage."""
        super().__init__(*args)

        self.exit_code = 409
        self.message = message