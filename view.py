import sqlite3
from datetime import datetime


DB_FILE = "entradas.db"

def listar_entradas():
    """
    Lista todas as entradas registradas.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM entradas')
        rows = cursor.fetchall()
        print("\nHistórico de Entradas:")
        for row in rows:
            print(f"ID: {row[0]}, Data: {row[1]}, Hora: {row[2]}")
    except sqlite3.Error as e:
        print(f"Erro ao listar entradas: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    print("\033c\033[43;30m")
    # Lista todas as entradas
    listar_entradas()

