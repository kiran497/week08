from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "service": "backend"}

@app.get("/health")
def health():
    return JSONResponse({"healthy": True})
