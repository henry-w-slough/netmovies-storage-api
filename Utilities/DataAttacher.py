import os
import config
import aiofiles


async def attach_data(new_dir: str, data_stream) -> None:

    async with aiofiles.open(os.path.join(new_dir, "movie.mp4"), "wb") as file:
        async for chunk in data_stream:
            await file.write(chunk)
