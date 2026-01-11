# 📂 File Extractor (Tkinter Edition)

![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**File Extractor** es una herramienta de escritorio robusta y sencilla diseñada para simplificar la gestión de archivos multimedia y metadatos. Permite buscar recursivamente, organizar y extraer tipos de archivos específicos desde estructuras de carpetas complejas hacia un destino unificado.

Ideal para editores de video, DITs (Digital Imaging Technicians) y organizadores de contenido que necesitan consolidar archivos dispersos (como `.mp4`, `.xml`, `.mxf`) en una sola ubicación de manera segura.

---

## 🚀 Características Principales

- **🔍 Búsqueda Recursiva Profunda**: Explora automáticamente todas las subcarpetas de la ruta de origen para encontrar cada archivo que coincida con la extensión seleccionada.
- **🛡️ Seguridad de Datos**:
  - **Prevención de Sobrescritura**: Verifica automáticamente si el archivo ya existe en el destino para evitar pérdidas accidentales.
  - **Validación**: Comprueba rutas y permisos antes de iniciar operaciones.
- **⚡ Modos de Operación Flexibles**:
  - **Copiar**: Duplica los archivos manteniendo los originales intactos (ideal para backups).
  - **Mover**: Traslada los archivos reorganizándolos en el destino.
- **🖥️ Interfaz Nativa**: GUI limpia y responsiva construida con Tkinter y ttk, con soporte para temas del sistema.
- **📋 Soporte de Formatos**: Optimizado para flujos de trabajo de video y media:
  - Video: `.mp4`, `.mxf`, `.lrv`, `.smi`
  - Metadatos/Otros: `.xml`, `.cue`, `.ppn`, `.bim`, `.thm`
- **📦 Portabilidad**: Disponible como ejecutable portable (.exe) o con instalador completo que crea accesos directos.

## 🛠️ Estructura del Proyecto

```text
FileExtractor-python/
├── .github/workflows/   # Integración continua (CI/CD)
├── installer/           # Scripts (setup.nsi) y recursos para el instalador
├── windows/             # Módulos de la interfaz gráfica
│   ├── __init__.py
│   ├── main_window.py   # Lógica principal de la ventana
│   ├── about_window.py  # Ventana "Acerca de"
│   └── utils.py         # Utilidades y monkey-patching
├── main.py              # Punto de entrada de la aplicación
├── version.py           # Definición de versión
├── requirements.txt     # Dependencias del proyecto
├── icon.ico             # Icono de la aplicación
└── LICENSE              # Licencia MIT
```

## 💻 Instalación y Desarrollo

### Requisitos Previos

- Python 3.11 o superior
- Git

### Configuración del Entorno

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/cristianvasquezc/FileExtractor-python.git

   cd FileExtractor-python
   ```

2. **Crear un entorno virtual (Recomendado)**:

   ```bash
   python -m venv .venv
   # En Windows:
   ,venv\Scripts\activate
   # En Linux/Mac:
   source .venv/bin/activate
   ```

3. **Instalar dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**:
   ```bash
   python main.py
   ```

## 📖 Guía de Uso

1. **Seleccionar Origen**: Haz clic en "Seleccionar" en el campo "Carpeta de entrada" para elegir la carpeta raíz donde buscar.
2. **Seleccionar Destino**: Elige la carpeta donde quieres que terminen los archivos.
3. **Filtrar por Extensión**: Usa el menú desplegable para elegir qué tipo de archivo extraer (ej. `.mp4`).
4. **Ejecutar Acción**:
   - **Copiar**: Para hacer una copia de seguridad.
   - **Mover**: Para reorganizar los archivos.
5. **Verificar**: La barra de estado inferior te mostrará el progreso y los resultados.

> **Tip**: Presiona `F1` en cualquier momento para ver la información de la versión y créditos.

## 📄 Licencia

Distribuido bajo la licencia MIT. Ver `LICENSE` para más información.

---

Desarrollado con ❤️ por Cristian Vásquez.
