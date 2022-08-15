from fastapi import FastAPI


app = FastAPI()


@app.get("/{pk}")
def index(pk: int):
    print(pk)
    return {"message": "Hello world"}
