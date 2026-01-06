import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sys
import os
import shutil

EXTENSIONS = [".mp4", ".mxf", ".lrv", ".xml", ".smi", ".cue", ".ppn", ".bim", ".thm"]

class MainWindow:
    def __init__(self, root):
        root.title("File Extractor")
        root.geometry("400x185")
        root.resizable(False, False)

        # ===== Entrada =====
        ttk.Label(root, text="Carpeta de entrada").place(x=10, y=8)

        self.entry_input = ttk.Entry(root)
        self.entry_input.place(x=10, y=28, width=290, height=24)

        ttk.Button(
            root, text="Seleccionar",
            command=self.select_input
        ).place(x=310, y=28, width=80, height=24)

        # ===== Salida =====
        ttk.Label(root, text="Carpeta de salida").place(x=10, y=58)

        self.entry_output = ttk.Entry(root)
        self.entry_output.place(x=10, y=78, width=290, height=24)

        ttk.Button(
            root, text="Seleccionar",
            command=self.select_output
        ).place(x=310, y=78, width=80, height=24)

        # ===== Extensión =====
        ttk.Label(root, text="Tipo de archivo").place(x=10, y=108)

        self.combo_ext = ttk.Combobox(
            root, values=EXTENSIONS, state="readonly"
        )
        self.combo_ext.current(0)
        self.combo_ext.place(x=10, y=128, width=200, height=24)
        self.combo_ext.bind("<<ComboboxSelected>>", self.update_ext)

        ttk.Button(
            root, text="Copiar",
            command=self.copy_files
        ).place(x=220, y=128, width=80, height=24)

        ttk.Button(
            root, text="Mover",
            command=self.move_files
        ).place(x=310, y=128, width=80, height=24)

        # ===== Status bar =====
        self.status = tk.Frame(root, relief="ridge", bd=1)
        self.status.place(x=0, y=160, width=400, height=25)

        self.lbl_help = ttk.Label(self.status, text="About: F1")
        self.lbl_help.place(x=8, y=2)

        self.lbl_cmd = ttk.Label(self.status, text="Cmd: -")
        self.lbl_cmd.place(x=100, y=2)

        self.lbl_ext = ttk.Label(self.status, text=f"Ext: {self.combo_ext.get()}")
        self.lbl_ext.place(x=180, y=2)

        root.bind("<F1>", self.show_about)

    # ================= LÓGICA =================

    def show_about(self, event=None):
        messagebox.showinfo(
            "About",
            "File Extractor\nVersión Tkinter"
        )

    def update_ext(self, event=None):
        self.lbl_ext.config(text=f"Ext: {self.combo_ext.get()}")
        self.lbl_cmd.config(text="Cmd: -")

    def select_input(self):
        folder = filedialog.askdirectory()
        if folder:
            self.entry_input.delete(0, tk.END)
            self.entry_input.insert(0, folder)

    def select_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.entry_output.delete(0, tk.END)
            self.entry_output.insert(0, folder)

    def copy_files(self):
        self.lbl_cmd.config(text="Cmd: Copiar")
        self.process_files(move=False)

    def move_files(self):
        self.lbl_cmd.config(text="Cmd: Mover")
        self.process_files(move=True)

    def is_valid_extension(self, ext):
        return ext in EXTENSIONS

    def process_files(self, move):
        input_dir = self.entry_input.get()
        output_dir = self.entry_output.get()
        ext = self.combo_ext.get()
    
        if not input_dir:
            messagebox.showwarning(
                "Datos incompletos",
                "Seleccione la carpeta de entrada."
            )
            return
    
        if not output_dir:
            messagebox.showwarning(
                "Datos incompletos",
                "Seleccione la carpeta de salida."
            )
            return
    
        if not self.is_valid_extension(ext):
            messagebox.showwarning(
                "Extensión inválida",
                "Seleccione un tipo de archivo válido."
            )
            return
    
        os.makedirs(output_dir, exist_ok=True)
    
        total_found = 0
        total_done = 0
    
        for root_dir, _, files in os.walk(input_dir):
            for file in files:
                if file.lower().endswith(ext):
                    total_found += 1
                    src = os.path.join(root_dir, file)
                    dst = os.path.join(output_dir, file)
    
                    if not os.path.exists(dst):
                        try:
                            if move:
                                shutil.move(src, dst)
                            else:
                                shutil.copy2(src, dst)
                            total_done += 1
                        except Exception as e:
                            messagebox.showerror("Error", str(e))
                            return
    
        if total_found == 0:
            messagebox.showinfo(
                "Sin archivos",
                f"No se encontraron archivos {ext} en la carpeta seleccionada."
            )
        elif total_done == 0:
            if move:
                messagebox.showinfo(
                    "Resultado",
                    "No se movieron archivos. Puede que ya existan en la carpeta destino."
                )
            else:
                messagebox.showinfo(
                    "Resultado",
                    "No se copiaron archivos. Puede que ya existan en la carpeta destino."
                )
        else:
            if move:
                messagebox.showinfo(
                    "Éxito",
                    f"Se movieron {total_done} archivos {ext} correctamente."
                )
            else:
                messagebox.showinfo(
                    "Éxito",
                    f"Se copiaron {total_done} archivos {ext} correctamente."
                )
