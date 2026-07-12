#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.database import DatabaseManager

if __name__ == "__main__":
    print("Inicializando base de datos...")
    db = DatabaseManager()
    print("Tablas creadas (si no existían).")
    print("Puedes comenzar a usar la aplicación.")
