from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Render!"}

@app.post("/print")
async def print_details(request: Request):
    body = await request.json()
    headers = dict(request.headers)
    query_params = dict(request.query_params)

    return {
        "message": "Received your POST request",
        "body": body,
        "headers": headers,
        "query_params": query_params
    }
