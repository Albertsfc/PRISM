from fastapi import APIRouter
from typing import Dict, Any
from app.database.db_manager import get_db_connection
from app.agents.orchestrator import orchestrate_end_of_month

router = APIRouter()

@router.get("/health")
def health_check() -> Dict[str, str]:
    """
    Health check da API, verifica conexão com banco de dados.
    """
    with get_db_connection() as conn:
        conn.execute("SELECT 1")
    return {"status": "ok", "service": "PRISM"}

@router.post("/end-of-month")
def trigger_end_of_month_orchestration() -> Dict[str, Any]:
    """
    Inicia orquestração do fim de mês pelo CrewAI.
    """
    result = orchestrate_end_of_month()
    return result
