from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from .pdf_viewer import VisorPDFWidget
from .search_panel import PanelBusqueda
from .calculators.conductor_calc import CalculadoraConductores
from core.calculator import CalculadorConductores
import os

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asistente NOM-001-SEDE-2012")
        self.resize(1200, 800)

        # Verificar existencia del PDF
        ruta_pdf = os.path.join("data", "nom_001_completa.pdf")
        if not os.path.exists(ruta_pdf):
            QMessageBox.warning(self, "PDF no encontrado",
                f"No se encontró el archivo:\n{ruta_pdf}\n\n"
                "Coloca el PDF en la carpeta 'data' y reinicia la aplicación.")

        # Widget central con splitter
        splitter_principal = QSplitter(Qt.Orientation.Horizontal)
        self.setCentralWidget(splitter_principal)

        # Panel izquierdo: pestañas de herramientas
        panel_izquierdo = QWidget()
        layout_izquierdo = QVBoxLayout(panel_izquierdo)
        tabs = QTabWidget()

        # Pestaña de búsqueda (se conectará después)
        self.panel_busqueda = PanelBusqueda(None)  # visor se asigna después
        tabs.addTab(self.panel_busqueda, "🔍 Buscar")

        # Pestaña de calculadoras
        calc_widget = QWidget()
        calc_layout = QVBoxLayout(calc_widget)
        self.calc_selector = QComboBox()
        self.calc_selector.addItems(["Calibre de conductor", "Puesta a tierra", "Protección térmica"])
        calc_layout.addWidget(self.calc_selector)

        btn_calcular = QPushButton("Calcular")
        btn_calcular.clicked.connect(self.realizar_calculo)
        calc_layout.addWidget(btn_calcular)

        self.resultado_calc = QTextEdit()
        self.resultado_calc.setReadOnly(True)
        calc_layout.addWidget(self.resultado_calc)

        tabs.addTab(calc_widget, "🧮 Calculadoras")
        layout_izquierdo.addWidget(tabs)
        splitter_principal.addWidget(panel_izquierdo)

        # Panel derecho: visor PDF
        self.visor = VisorPDFWidget(ruta_pdf)
        splitter_principal.addWidget(self.visor)

        # Conectar búsqueda con visor
        self.panel_busqueda.visor = self.visor

        # Proporciones
        splitter_principal.setSizes([300, 700])

        self.crear_menu()

    def crear_menu(self):
        menubar = self.menuBar()
        menu_archivo = menubar.addMenu("Archivo")
        abrir_action = QAction("Abrir PDF...", self)
        abrir_action.triggered.connect(self.abrir_pdf)
        menu_archivo.addAction(abrir_action)
        menu_archivo.addSeparator()
        salir_action = QAction("Salir", self)
        salir_action.triggered.connect(self.close)
        menu_archivo.addAction(salir_action)

        menu_ayuda = menubar.addMenu("Ayuda")
        acerca_action = QAction("Acerca de", self)
        acerca_action.triggered.connect(self.mostrar_acerca)
        menu_ayuda.addAction(acerca_action)

    def abrir_pdf(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir PDF", "", "Archivos PDF (*.pdf)")
        if ruta:
            self.visor.cargar_pdf(ruta)

    def realizar_calculo(self):
        calculo = self.calc_selector.currentText()
        if calculo == "Calibre de conductor":
            amperaje, ok = QInputDialog.getInt(self, "Calibre de conductor", "Corriente (amperios):", 20, 1, 1000)
            if ok:
                calibre = CalculadorConductores.calcular_calibre(amperaje)
                self.resultado_calc.setText(f"Calibre recomendado: {calibre}")
        elif calculo == "Puesta a tierra":
            self.resultado_calc.setText(
                "Resistencia máxima permitida: 25 ohms\n"
                "Si es mayor, instalar electrodos adicionales.\n"
                "Ver Artículo 250 de la NOM-001-SEDE-2012")
        elif calculo == "Protección térmica":
            self.resultado_calc.setText(
                "Protección contra sobrecorriente:\n"
                "Los interruptores deben tener capacidad no menor a la corriente del circuito.\n"
                "Ver Artículo 240.")

    def mostrar_acerca(self):
        QMessageBox.about(self, "Acerca de",
            "Asistente NOM-001-SEDE-2012 v1.0\n\n"
            "Herramienta offline para consulta de la Norma Oficial Mexicana\n"
            "de Instalaciones Eléctricas.\n\n"
            "Creado con Python y PyQt6")
