from fastapi import FastAPI, Request

from rpc.client import greet

app = FastAPI()

@app.get("/")
def get(request:Request):
    return {'message': 'Hello World!'}

@app.get('/greetings')
async def greetings():
    response = await greet()
    return response.message