import sqlite3
import PyPDF2
import re

class ProcesadorPDF:
    """Clase para extraer texto y tablas del PDF (futura implementación)"""
    def __init__(self, ruta_pdf):
        self.ruta_pdf = ruta_pdf

    def extraer_texto(self):
        with open(self.ruta_pdf, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            texto = ""
            for pagina in reader.pages:
                texto += pagina.extract_text()
            return texto

    # Aquí se pueden agregar métodos para extraer tablas específicas (ej. Tabla 310-16)
