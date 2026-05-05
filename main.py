from fastapi import FastAPI

app = FastAPI(root_path="/app/")


@app.get("/asdd/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.post("/dasd/")
def greet_user(name: str):
    return {"message": "Hello, " + name + "!"}



