from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QTimer

class PanelBusqueda(QWidget):
    def __init__(self, visor, parent=None):
        super().__init__(parent)
        self.visor = visor
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        self.buscador = QLineEdit()
        self.buscador.setPlaceholderText("Buscar en la norma...")
        self.buscador.textChanged.connect(self.on_text_changed)
        layout.addWidget(self.buscador)

        self.resultados = QListWidget()
        self.resultados.itemClicked.connect(self.ir_a_pagina)
        layout.addWidget(self.resultados)

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.realizar_busqueda)

    def on_text_changed(self, texto):
        self.timer.start(500)

    def realizar_busqueda(self):
        texto = self.buscador.text()
        if len(texto) < 3:
            return
        # Aquí se implementaría la búsqueda real en el PDF (simulada)
        self.resultados.clear()
        # Ejemplo ficticio:
        self.resultados.addItem("Página 42: Definiciones - Puesta a tierra")
        self.resultados.addItem("Página 105: Tabla 310-16 Conductores")

    def ir_a_pagina(self, item):
        # Extraer número de página del texto del item (simple)
        import re
        match = re.search(r'Página (\d+)', item.text())
        if match and self.visor:
            pagina = int(match.group(1))
            # self.visor.ir_a_pagina(pagina)  # requiere implementación en visor
