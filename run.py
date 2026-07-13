import uvicorn
import os
import sqlite3
from app.database.db_manager import init_db
from app.config import settings

def main() -> None:
    """
    Entry point do sistema PRISM. Inicializa o DB e sobe o servidor FastAPI.
    """
    print("Iniciando setup do PRISM...")
    
    # Initialize the local database schema
    init_db()

    print("Banco de dados local prism_workforce.db garantido com sucesso.")
    print(f"Iniciando PRISM v{settings.version} na porta {settings.port}...")

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.port,
        reload=settings.debug
    )

if __name__ == "__main__":
    main()
