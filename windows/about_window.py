import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk
from .utils import resource_path
from version import VERSION

class AboutWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.withdraw()
        self.title("Acerca de File Extractor")
        self.resizable(False, False)
        self.center_window(250, 410)        
        self.set_app_icon()
        self.deiconify()
        
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(expand=True, fill="both")

        # Icono
        try:
            icon_path = resource_path("icon.ico")
            img = Image.open(icon_path)
            img = img.resize((64, 64), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            icon_label = ttk.Label(main_frame, image=self.photo)
            icon_label.pack(pady=(0, 10))
        except Exception:
            pass
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text="File Extractor", 
            font=("Segoe UI", 12, "bold")
        )
        title_label.pack(pady=(0, 5))
        
        # Descripción refinada
        description = (
            "FileExtractor es una potente herramienta de escritorio diseñada para "
            "automatizar la organización de archivos mediante la copia o el traslado "
            "basado en extensiones específicas.\n\n"
            "Con una interfaz intuitiva, permite gestionar directorios de manera "
            "recursiva, explorando automáticamente todas las subcarpetas para "
            "garantizar que ningún archivo sea omitido. Es la solución ideal para "
            "ahorrar tiempo en tareas repetitivas y gestionar grandes volúmenes "
            "de información con total seguridad y confianza."
        )
        
        desc_label = ttk.Label(
            main_frame, 
            text=description,
            wraplength=230,
            font=("Segoe UI", 9)
        )
        desc_label.pack(pady=(0, 5))
        
        # Versión e Info
        info_frame = ttk.Frame(main_frame)
        info_frame.pack(fill="x")
        
        ttk.Label(info_frame, text="Versión:", font=("Segoe UI", 9, "bold")).pack(side="left")
        ttk.Label(info_frame, text=f" {VERSION}").pack(side="left")
        
        # Link Developer
        dev_frame = ttk.Frame(main_frame)
        dev_frame.pack(fill="x", pady=(5, 0))
        
        ttk.Label(dev_frame, text="Desarrollado por:", font=("Segoe UI", 9, "bold")).pack(side="left")
        
        link_label = tk.Label(
            dev_frame, 
            text=" Cristian Vásquez", 
            fg="#de1a86", 
            cursor="hand2",
            font=("Segoe UI", 8)
        )
        link_label.pack(side="left")
        link_label.bind("<Button-1>", lambda e: webbrowser.open("https://mislinks.netlify.app/"))

        self.focus_set()
        self.grab_set()
        self.bind("<Escape>", lambda e: self.destroy())

