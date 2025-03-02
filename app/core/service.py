from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_index():
    return {"message": "Hello, world!"}


@app.get("/healthz")
def read_root():
    return {"status": "healthy"}
