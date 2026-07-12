# Asistente NOM-001-SEDE-2012

Aplicación de escritorio offline para consultar la Norma Oficial Mexicana NOM-001-SEDE-2012 (Instalaciones Eléctricas).

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes)

## 🚀 Instalación

1. Clona o descarga este proyecto.
2. Abre una terminal en la carpeta raíz.
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Inicializa la base de datos (crea las tablas vacías):
   ```bash
   python scripts/init_db.py
   ```
5. Coloca el archivo PDF de la norma en la carpeta `data/` con el nombre exacto:
   `nom_001_completa.pdf`
   
   > **🔗 Enlace de descarga oficial** (gratuito):  
   > [https://www.normasoficiales.mx/nom/nom-001-sede-2012](https://www.normasoficiales.mx/nom/nom-001-sede-2012)

6. Ejecuta la aplicación:
   ```bash
   python main.py
   ```

## 🧩 Funcionalidades

- **Visor PDF** con navegación por páginas y zoom.
- **Buscador inteligente** (encuentra texto en el PDF).
- **Calculadoras eléctricas** basadas en la norma:
  - Calibre de conductores (Tabla 310-16)
  - Puesta a tierra (Artículo 250)
  - Protección contra sobrecorriente
- **Marcadores personales** (próximamente)
- **Interfaz moderna** con QSS personalizable.

## 🛠️ Personalización

Puedes modificar el archivo `styles.qss` para cambiar colores y apariencia.

## 📄 Licencia

Uso libre para fines educativos y profesionales. La norma es propiedad de la Secretaría de Energía (México).

---

✨ Desarrollado con PyQt6 y mucho café.
