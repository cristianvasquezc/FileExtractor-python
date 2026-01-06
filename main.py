import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sys
import os
import shutil
from windows.main_window import MainWindow

def center_window(root, width, height):
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    root.geometry(f"{width}x{height}+{x}+{y}")

def resource_path(rel_path):
    try:
        base = sys._MEIPASS
    except:
        base = os.path.abspath(".")
    return os.path.join(base, rel_path)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(resource_path("icon.ico"))
    MainWindow(root)
    center_window(root, 400, 185)
    root.deiconify()   
    root.mainloop()
