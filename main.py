from fastapi import FastAPI

app = FastAPI

@app.get("/")
def root():
    return {"message": "EWS Backend is alive"}

@app.get("/status")
def status():
    return {"status": "ok", "engineer": "Luis Orozco"}
