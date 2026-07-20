from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/")
def chat_copilot(request: ChatRequest):
    """
    Mock do Copilot NLP.
    Em produção, encaminha 'request.message' para o CrewAI (Intent Router).
    """
    msg = request.message.lower()
    
    if "cortar" in msg or "reduzir" in msg:
        return {"status": "success", "action_taken": "schedule_optimized", "details": "Otimizador rodou reduzindo horas conforme compliance."}
    
    return {"status": "success", "action_taken": "none", "reply": "Entendido. Como posso ajudar com a escala hoje?"}
