import os
import ffmpeg
import hashlib

from .. import config


class MovieParser:


    def __init__(self, root_dir:str) -> None:
        """
            Handles all operations involving reading, chunking, and storing movies.
            Args:
                root_dir (str): The directory into which movies are parsed into and where all movies are housed. 
                                For example, a given movie file would be chunked and added to (root_dir/MovieName).
        """

        self.root_dir = root_dir    
        #creating root directory
        os.makedirs(self.root_dir, exist_ok=True)


    def get_movie_directory(self, movie_name:str) -> str:
        """Returns the directory of the movie given relative to the root directory of the MovieParser."""
        return os.path.join(self.root_dir, movie_name)
    

    def parse_movie(self, movie_file:str) -> None:
        os.makedirs(self.get_movie_directory(movie_file))


    def get_chunk_id(self, data:bytes, length:int=8) -> str:
        """Returns a hash id based on the data and length provided."""
        return hashlib.sha256(data).hexdigest()[:length]


    def data_to_chunks(self, data:str, http_request:str, id_length:int=8) -> None:
        """Takes a file and breaks it into data chunks which are placed in a given directory. Chunks are named with hash convention."""

        #making the subdirectory for the movie relative to the root directory of the Parser
        movie_dir = os.path.join(self.root_dir, http_request.name)
        os.makedirs(movie_dir, exist_ok=True)


        


        