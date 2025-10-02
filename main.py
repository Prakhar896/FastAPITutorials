from fastapi import FastAPI, Request
import random, string

app = FastAPI()

@app.middleware("http")
async def request_id_logging(request: Request, call_next):
    response = await call_next(request)
    request_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    response.headers["X-Request-ID"] = request_id
    print(f"Request ID: {request_id} - Path: {request.url.path}")
    return response

@app.get("/")
async def say_hi():
    return "Hello, World!"