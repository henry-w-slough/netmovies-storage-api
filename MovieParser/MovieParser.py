import os


class MovieParser:


    def __init__(self, root_dir:str) -> None:
        """
            Handles all operations involving reading, chunking, and storing movies.
            Args:
                root_dir (str): The directory into which movies are parsed into and where all movies are housed. 
                                For example, a given movie file would be chunked and added to (root_dir/MovieName).
        """

        self.root_dir = root_dir    

        os.makedirs(self.root_dir, exist_ok=True)


    def get_movie_directory(self, movie_name:str) -> str:
        """Returns the directory of the movie given relative to the root directory of the MovieParser."""
        return os.path.join(self.root_dir, movie_name)
        


        