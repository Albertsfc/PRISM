from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class ClockInRequest(BaseModel):
    employee_id: int
    lat: float
    lon: float

# Coordenadas mock da "sede da empresa"
OFFICE_LAT = 37.7749
OFFICE_LON = -122.4194
MAX_DISTANCE_DEGREES = 0.01  # Simulação simples de distância

@router.post("/clock-in")
def mobile_clock_in(request: ClockInRequest):
    """
    Mock de batida de ponto com Geofencing.
    """
    dist = abs(request.lat - OFFICE_LAT) + abs(request.lon - OFFICE_LON)
    
    if dist > MAX_DISTANCE_DEGREES:
        raise HTTPException(status_code=403, detail="Você está fora do raio permitido da empresa (Geofence violation).")
        
    return {"status": "success", "message": f"Ponto registrado para emp_id {request.employee_id} com sucesso."}
