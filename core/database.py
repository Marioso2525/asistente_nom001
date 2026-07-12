import sqlite3
from contextlib import contextmanager
from pathlib import Path

class DatabaseManager:
    def __init__(self, db_path="data/extracted_tables.db"):
        self.db_path = db_path
        self._crear_tablas_si_no_existen()

    def _crear_tablas_si_no_existen(self):
        with self.obtener_conexion() as conn:
            # Tabla para capacidad de conductores (Tabla 310-16)
            conn.execute('''
                CREATE TABLE IF NOT EXISTS capacidad_conductores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    calibre TEXT,
                    material TEXT,
                    temperatura INTEGER,
                    amperaje REAL,
                    aplicacion TEXT
                )
            ''')
            # Tabla para puesta a tierra
            conn.execute('''
                CREATE TABLE IF NOT EXISTS puesta_tierra (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo_suelo TEXT,
                    resistencia_maxima REAL,
                    metodo_mejora TEXT
                )
            ''')
            # Tabla para factores de corrección
            conn.execute('''
                CREATE TABLE IF NOT EXISTS factores_correccion (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT,
                    condicion TEXT,
                    factor REAL
                )
            ''')

    @contextmanager
    def obtener_conexion(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    def ejecutar_consulta(self, consulta, parametros=()):
        with self.obtener_conexion() as conn:
            cursor = conn.execute(consulta, parametros)
            return cursor.fetchall()

    def insertar(self, tabla, datos):
        with self.obtener_conexion() as conn:
            columnas = ', '.join(datos.keys())
            placeholders = ', '.join(['?' for _ in datos])
            consulta = f"INSERT INTO {tabla} ({columnas}) VALUES ({placeholders})"
            cursor = conn.execute(consulta, list(datos.values()))
            return cursor.lastrowid
