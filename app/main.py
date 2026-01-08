from fastapi import FastAPI
import datetime
import socket

app = FastAPI()

@app.get("/")
def home():
    return {
        "app": "Smart DevOps Platform",
        "version": "1.0.0",
        "time": datetime.datetime.utcnow().isoformat(),
        "host": socket.gethostname()
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
