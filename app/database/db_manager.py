import os
import sqlite3
from contextlib import contextmanager
from typing import Generator
from sqlalchemy import create_engine
from app.config import settings

engine = create_engine(
    settings.database_url, connect_args={"check_same_thread": False}
)

def init_db() -> None:
    """
    Inicializa o banco de dados local executando o schema SQL, caso o arquivo exista.
    """
    # If using sqlite:///, we extract the file path
    db_path = settings.database_url.replace("sqlite:///", "")
    
    # We will execute the schema.sql using python sqlite3 directly to ensure all statements run
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    
    if os.path.exists(schema_path):
        with open(schema_path, "r", encoding="utf-8") as f:
            sql_script = f.read()
            
        with sqlite3.connect(db_path) as conn:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("PRAGMA synchronous=NORMAL;")
            conn.executescript(sql_script)
            conn.commit()
    else:
        print("Aviso: schema.sql não encontrado.")

@contextmanager
def get_db_connection() -> Generator[sqlite3.Connection, None, None]:
    """
    Yields a database connection with WAL mode enabled.
    Ensures the connection is safely closed after execution or exception.
    """
    db_path = settings.database_url.replace("sqlite:///", "")
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA synchronous=NORMAL;")
        conn.row_factory = sqlite3.Row
        yield conn
    finally:
        conn.close()
