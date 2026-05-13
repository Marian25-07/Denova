import sqlite3
from config import Config

def get_connection():
    """
    Establece y retorna una conexión con la base de datos SQLite.
    Usa la ruta definida en config.py
    """
    return sqlite3.connect(Config.SQLITE_DATABASE)

def create_tables():
    """
    Crea la tabla logs_syra si no existe.
    Esta tabla almacenará los registros de interacción del chatbot SYRA.
    """
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS logs_syra (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                mensaje TEXT NOT NULL,
                respuesta TEXT NOT NULL,
                fecha TEXT NOT NULL
            )
        """)
        conn.commit()

# Crear automáticamente la tabla al importar el archivo
create_tables()import sqlite3
from config import Config

def get_connection():
    """
    Establece y retorna una conexión con la base de datos SQLite.
    Usa la ruta definida en config.py
    """
    return sqlite3.connect(Config.SQLITE_DATABASE)

def create_tables():
    """
    Crea la tabla logs_syra si no existe.
    Esta tabla almacenará los registros de interacción del chatbot SYRA.
    """
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS logs_syra (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                mensaje TEXT NOT NULL,
                respuesta TEXT NOT NULL,
                fecha TEXT NOT NULL
            )
        """)
        conn.commit()

# Crear automáticamente la tabla al importar el archivo
create_tables()