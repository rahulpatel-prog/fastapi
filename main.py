from fastapi import FastAPI, Request
import json
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Render!"}

@app.post("/print")
async def print_details(request: Request):
    # Try reading JSON safely
    try:
        body = await request.json()
    except:
        body = "No valid JSON body received"

    headers = dict(request.headers)
    query_params = dict(request.query_params)

    # Log all data
    logger.info("---- Incoming Request ----")
    logger.info("Body: %s", json.dumps(body, indent=2) if isinstance(body, dict) else body)
    logger.info("Headers: %s", json.dumps(headers, indent=2))
    logger.info("Query Params: %s", json.dumps(query_params, indent=2))
    logger.info("--------------------------")

    return {
        "message": "Received your POST request",
        "body": body,
        "headers": headers,
        "query_params": query_params
    }

