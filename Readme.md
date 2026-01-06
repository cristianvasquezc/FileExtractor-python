# File Extractor (Tkinter Edition)

Una herramienta sencilla y eficiente para buscar, organizar y extraer tipos de archivos específicos desde una estructura de carpetas compleja hacia un único destino.

## 🚀 Características

- **Interfaz Gráfica (GUI)**: Construida con Tkinter (ttk) para una apariencia nativa y limpia.
- **Búsqueda Recursiva**: Explora subcarpetas automáticamente para encontrar los archivos que necesitas.
- **Operaciones de Archivo**: Soporta tanto **Copiar** como **Mover** archivos.
- **Prevención de Sobrescritura**: No sobrescribe archivos que ya existen en la carpeta de destino.
- **Extensiones Soportadas**: Configurado para manejar formatos comunes de video, metadata y auxiliares:
  - `.mp4`, `.mxf`, `.lrv`, `.xml`, `.smi`, `.cue`, `.ppn`, `.bim`, `.thm`

## 🛠️ Requisitos

- Python 3.x
- Tkinter (incluido en la mayoría de las instalaciones de Python)

## 📖 Cómo usar

1. **Carpeta de Entrada**: Selecciona la carpeta raíz donde se encuentran tus archivos originales.
2. **Carpeta de Salida**: Selecciona dónde quieres que se guarden los archivos extraídos.
3. **Tipo de archivo**: Selecciona la extensión que deseas extraer del menú desplegable.
4. **Acción**: Haz clic en **Copiar** para duplicar los archivos o **Mover** para trasladarlos definitivamente.

> [!TIP]
> Puedes presionar **F1** dentro de la aplicación para ver información sobre la versión.

## 📦 Compilación con PyInstaller

Para generar un ejecutable (.exe) de un solo archivo y con el icono aplicado, usa los siguientes comandos:

### Crear sin recursos externos (Recomendado)
```bash
pyinstaller --onefile --windowed --icon=icon.ico --add-data "icon.ico;." main.py
```
*Desarrollado para la extracción rápida de archivos en entornos de edición y organización de media.*
