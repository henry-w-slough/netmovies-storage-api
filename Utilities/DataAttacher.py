


async def attach_data(new_dir:str, data:bytes) -> None:
    
    with open(new_dir, "wb") as file:
        file.write(data)