import os
import config

async def attach_data(new_dir:str, data:bytes) -> None:
    
    with open(os.path.join(new_dir, f"movie.mp4"), "wb") as file:
        file.write(data)