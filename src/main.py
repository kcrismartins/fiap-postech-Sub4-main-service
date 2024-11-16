from fastapi import FastAPI, HTTPException
from src.database import init_db
from src.services.create_edit import create_vehicle, edit_vehicle

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

@app.post("/vehicles")
async def post_vehicle(vehicle_data: dict):
    return await create_vehicle(vehicle_data)

@app.put("/vehicles/{vehicle_id}")
async def put_vehicle(vehicle_id: int, vehicle_data: dict):
    try:
        return await edit_vehicle(vehicle_id, vehicle_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
