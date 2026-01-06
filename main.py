import tkinter as tk
from windows.utils import center_window, set_app_icon 
from windows.main_window import MainWindow

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    MainWindow(root)
    root.deiconify()   
    root.mainloop()
