from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "EWS Backend is alive"}

@app.get("/status")
def status():
    return {"status": "ok", "engineer": "Luis Orozco"}

class Ingeniniero(BaseModel):
    name: str
    age: int
    specialty: str

@app.post("/engineer")
def create_engineer(engineer: Ingeniniero):
    return {
        "message": f"Bienvendio {engineer.name}",
        "data": engineer
    }