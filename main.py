import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import VentanaPrincipal

def main():
    app = QApplication(sys.argv)
    with open("styles.qss", "r") as f:
        app.setStyleSheet(f.read())
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
