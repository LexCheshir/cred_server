import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def get_creds():
    return {"login": "login", "password": "password"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
