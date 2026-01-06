import shutil
import sys
import os
import tkinter as tk

def center_window(self, width, height):
    self.update_idletasks()
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    self.geometry(f"{width}x{height}+{x}+{y}")

def resource_path(rel_path):
    try:
        base = sys._MEIPASS 
    except AttributeError:
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
    return os.path.join(base, rel_path)

def set_app_icon(self, icon_name="icon.ico"):
    from tkinter import TclError
    icon_path = resource_path(icon_name)
    if os.path.exists(icon_path):
        try:
            self.iconbitmap(icon_path)
        except TclError:
            pass

# Monkey-patching
tk.Tk.center_window = center_window
tk.Toplevel.center_window = center_window
tk.Tk.set_app_icon = set_app_icon
tk.Toplevel.set_app_icon = set_app_icon
