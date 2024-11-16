from pydantic import BaseModel
from typing import Optional

class VehicleCreateSchema(BaseModel):
    brand: str
    model: str
    year: int
    color: str
    price: float

class VehicleUpdateSchema(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    color: Optional[str] = None
    price: Optional[float] = None

class VehicleResponseSchema(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    color: str
    price: float

    class Config:
        orm_mode = True
