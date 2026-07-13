from fastapi import APIRouter
from typing import List, Dict, Any
from app.database.db_manager import get_db_connection
from app.agents.burnout_risk import analyze_burnout_risks

router = APIRouter()

@router.get("/")
def get_alerts() -> List[Dict[str, Any]]:
    """
    Recupera alertas de burnout com status open.
    """
    with get_db_connection() as conn:
        alerts = conn.execute("SELECT a.*, e.name FROM burnout_alerts a JOIN employees e ON a.employee_id = e.id WHERE a.status = 'open' ORDER BY a.risk_score DESC").fetchall()
    return [dict(a) for a in alerts]

@router.post("/analyze")
def run_burnout_analysis() -> Dict[str, Any]:
    """
    Dispara a análise de risco de burnout para a última semana.
    """
    result = analyze_burnout_risks()
    return result
