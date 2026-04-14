from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.shipment import ShipmentCreate, ShipmentResponse
from app.services import shipment_service

router = APIRouter(prefix="/shipments", tags=["Shipments"])


@router.post("/", response_model=ShipmentResponse)
def create_shipment(shipment: ShipmentCreate, db: Session = Depends(get_db)):
    try:
        return shipment_service.create_shipment(db, shipment)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))