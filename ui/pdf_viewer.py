from PyQt6.QtWidgets import QWidget, QVBoxLayout
import qpageview

class VisorPDFWidget(QWidget):
    def __init__(self, ruta_pdf, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.visor = qpageview.View()
        layout.addWidget(self.visor)
        self.cargar_pdf(ruta_pdf)

    def cargar_pdf(self, ruta):
        try:
            self.visor.loadPdf(ruta)
            self.visor.setZoomMode(qpageview.View.ZoomMode.FIT_WIDTH)
        except Exception as e:
            print(f"Error cargando PDF: {e}")

    def ir_a_pagina(self, num_pagina):
        # Implementar según API de qpageview (puede ser self.visor.goToPage(num_pagina))
        pass

    def buscar(self, texto):
        """Busca texto en el PDF y devuelve lista de resultados (simulado)"""
        # Esta funcionalidad depende de la versión de qpageview; se puede ampliar luego.
        return []
