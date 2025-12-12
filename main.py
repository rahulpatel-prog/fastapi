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

# @app.post("/print")
# async def print_details(request: Request):
#     # Try reading JSON safely
#     try:
#         body = await request.json()
#     except:
#         body = "No valid JSON body received"
#
#     headers = dict(request.headers)
#     query_params = dict(request.query_params)
#
#     # Log all data
#     logger.info("---- Incoming Request ----")
#     logger.info("Body: %s", json.dumps(body, indent=2) if isinstance(body, dict) else body)
#     logger.info("Headers: %s", json.dumps(headers, indent=2))
#     logger.info("Query Params: %s", json.dumps(query_params, indent=2))
#     logger.info("--------------------------")
#
#     return {
#         "message": "Received your POST request",
#         "body": body,
#         "headers": headers,
#         "query_params": query_params
#     }


@app.post("/print")
async def print_details(request: Request):
    # Read raw body
    body_bytes = await request.body()

    # Try reading JSON
    try:
        body = await request.json()  # FastAPI auto-parses JSON
        logger.info("---- JSON Body ----")
        logger.info(json.dumps(body, indent=2))
    except Exception:
        # If not JSON, log raw body as text
        body_text = body_bytes.decode("utf-8") if body_bytes else "Empty body"
        logger.info("---- Non-JSON Body ----")
        logger.info(body_text)

    # Log headers and query params
    headers = dict(request.headers)
    query_params = dict(request.query_params)

    logger.info("---- Headers ----")
    logger.info(json.dumps(headers, indent=2))
    logger.info("---- Query Params ----")
    logger.info(json.dumps(query_params, indent=2))

    return {
        "message": "Request logged successfully",
        "headers": headers,
        "query_params": query_params
    }
