
import sqlite3
from datetime import datetime

# Nome do arquivo da base de dados
DB_FILE = "entradas.db"

def init_db():
    """
    Inicializa a base de dados.
    Cria a tabela 'entradas' se não existir.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS entradas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                hora TEXT NOT NULL
            )
        ''')
        conn.commit()
        print("Base de dados inicializada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao inicializar a base de dados: {e}")
    finally:
        conn.close()

def registrar_entrada():
    """
    Registra a data e hora atuais na tabela 'entradas'.
    """
    data_atual = datetime.now().strftime("%Y-%m-%d")  # Formato: YYYY-MM-DD
    hora_atual = datetime.now().strftime("%H:%M:%S")  # Formato: HH:MM:SS

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO entradas (data, hora) VALUES (?, ?)', (data_atual, hora_atual))
        conn.commit()
        print(f"Entrada registrada com sucesso: Data={data_atual}, Hora={hora_atual}")
    except sqlite3.Error as e:
        print(f"Erro ao registrar entrada: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    print("\033c\033[43;30m")
    # Inicializa a base de dados
    init_db()
    
    # Registra uma nova entrada
    registrar_entrada()
