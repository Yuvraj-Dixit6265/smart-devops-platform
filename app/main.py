from fastapi import FastAPI
from app.logger import logger

import datetime
import socket

app = FastAPI(title="Smart DevOps Platform", version="1.0.0")


@app.get("/")
def home():
    logger.info("Home endpoint called")
    return {
        "app": "Smart DevOps Platform",
        "version": "1.0.0",
        "time": datetime.datetime.utcnow().isoformat(),
        "host": socket.gethostname()
    }


@app.get("/health")
def health():
    logger.info("Health check endpoint called")
    return {"status": "healthy"}


@app.get("/crash")
def crash():
    logger.error("Application crash simulated")
    raise Exception("Simulated crash for monitoring")
