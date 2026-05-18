import aiofiles
import os
import fastapi
from typing import AsyncGenerator

import config


async def assemble_data(directory:str, data_stream:AsyncGenerator[bytes, None]) -> None:
    """Takes a data stream from HTTP and connects it, outputting the connected file to the given directory."""
    #opening the new file
    async with aiofiles.open(os.path.join(directory, f"{config.MOVIE_FILENAME}.mp4"), "wb") as file:
        #writing the data stream, note that it will write as the data is received
        async for chunk in data_stream:
            await file.write(chunk)
