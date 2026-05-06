from pydantic import BaseModel, Field
import uuid


class MovieMetadata(BaseModel):
    """
        Instance of metadata relating to a movie. Acts as a contract for incoming HTTP requests to follow for data.
        Note that by default, pydantic will ignore any excess fields given in a request if they are not within this model.
    """
    name:str = Field(min_length=1, max_length=255)
    movie_uuid:uuid.UUID