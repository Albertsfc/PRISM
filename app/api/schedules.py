from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict, Any
from app.database.db_manager import get_db_connection
from app.agents.scheduling_optimizer import optimize_schedule

router = APIRouter()

class OptimizeRequest(BaseModel):
    target_date: str
    required_staff: int

@router.get("/")
def get_schedules() -> List[Dict[str, Any]]:
    """
    Retorna as últimas 50 escalas de trabalho.
    """
    with get_db_connection() as conn:
        schedules = conn.execute("SELECT s.*, e.name FROM schedules s JOIN employees e ON s.employee_id = e.id ORDER BY schedule_date DESC LIMIT 50").fetchall()
    return [dict(s) for s in schedules]

@router.post("/optimize")
def run_scheduling_optimizer(req: OptimizeRequest) -> Dict[str, Any]:
    """
    Otimiza o agendamento de funcionários utilizando PuLP.
    """
    result = optimize_schedule(target_date=req.target_date, required_staff=req.required_staff)
    return result
