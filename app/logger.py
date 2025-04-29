from fastapi import Request
from datetime import datetime


async def log_request(request: Request):
    method = request.method
    endpoint = request.url.path
    timestamp = datetime.utcnow()
    print(f"{timestamp} - {method} request to {endpoint}")
