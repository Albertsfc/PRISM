from fastapi import APIRouter
from typing import List, Dict, Any
from app.database.db_manager import get_db_connection
from app.agents.labor_forecaster import forecast_labor_costs

router = APIRouter()

@router.get("/labor-costs")
def get_labor_costs() -> List[Dict[str, Any]]:
    """
    Recupera as projeções de custos laborais futuras.
    """
    with get_db_connection() as conn:
        forecasts = conn.execute("SELECT * FROM labor_forecasts ORDER BY forecast_month ASC").fetchall()
    return [dict(f) for f in forecasts]

@router.post("/generate")
def generate_forecasts() -> Dict[str, Any]:
    """
    Gera novas projeções de custos baseadas no histórico.
    """
    result = forecast_labor_costs(months_ahead=12)
    return result
