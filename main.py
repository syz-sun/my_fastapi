import fastapi
from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def regist():
    return {"message": "Hello, World!"}



if __name__ == '__main__':
    pass


