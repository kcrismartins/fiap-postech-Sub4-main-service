from src.models import Vehicle
from src.database import session

async def create_vehicle(data: dict):
    vehicle = Vehicle(**data)
    session.add(vehicle)
    session.commit()
    return {"message": "Vehicle created successfully", "vehicle_id": vehicle.id}

async def edit_vehicle(vehicle_id: int, data: dict):
    vehicle = session.query(Vehicle).filter_by(id=vehicle_id).first()
    if not vehicle:
        raise ValueError("Vehicle not found")
    for key, value in data.items():
        setattr(vehicle, key, value)
    session.commit()
    return {"message": "Vehicle updated successfully"}
